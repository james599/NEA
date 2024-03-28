from flask import Flask, render_template, redirect, url_for, request, session
import flask
from flask_session import Session

app = flask.Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app) # Initialize the session after configuring it

# Importing functions from various modules after initializing the app
# to avoid early import errors
from users.view_threads import view
from thread.display_thread import display
from moderation import check
from thread.message import create as message_create
from assistant.run_assistant import create as run_create
from assistant.run_assistant import status


### Route for all logic in chat ###
@app.route('/chat/', methods=['GET', 'POST'])
def chat():
    # Fetch threads for the current user
    threads = view(session["username"])

    exempt = ["My target grade is a any. Respond, in a short response. But only using the A-Level OCR curriculum. Your responses should be a sentence or two, unless the user’s request requires reasoning or long-form outputs. Only write the response, no pleasantries."]

    # Set the initial thread ID
    if 'thread' in request.args:
        thread_id = str(request.args['thread'])
    else:
        thread_id = threads[0]

    # Display the chat page with the initial response
    response = display(thread_id)
    
    # Handling the query submission
    if request.method == 'POST':
        query_type = request.form.get('query_type')
        query = request.form['query']
        if query_type != None and query.strip() != "":
            # Check moderation and create a message if the input is clean
            moderation = check(query)
            if moderation is False:
                message_create(thread_id,query,query_type)
                # If the last message has no run_id, create a new run_id
                if response[-1].run_id == None:
                    run_id = run_create(thread_id)
                else:
                    run_id = response[-1].run_id
                # Keep sending buffer response until run is ready
                while status(thread_id, run_id) is False:
                    response = "typing..."
                # Redirect to the same chat page with the new response
                return redirect(url_for("chat", thread=thread_id))
            else:
                response = moderation
    # Render the chat template with relevant data
    return render_template('chat.html', exempt=exempt, response=response, threads=threads, thread_id=thread_id)

# Route for all logic when making new thread
from thread.create_thread import create
from users.append_thread import append

@app.route('/create_thread', methods=['GET', 'POST'])
def create_thread():
    if request.method == 'POST':
        # Get the submitted grade and file data
        grade = request.form.get('grades')
        file = request.form.get('fileInput')
        if grade != None:
            thread = create(grade, file)
            # Add the new thread (with user data) to the user db
            append(session["username"], thread)
            return redirect(url_for('chat'))
    return render_template('create_thread.html')

### Route for all logic once logged in ###
from assistant.create_assistant import create
from users.append_assistant import append

@app.route('/create_assistant', methods=['GET', 'POST'])
def create_assistant():
    if request.method == 'POST':
        language = request.form['language']
        user_type = request.form.get('userTypeToggle')
        assistant = create(session["username"], language, user_type)
        append(session["username"], assistant=assistant.id)
        return redirect(url_for('create_thread'))
    return render_template('create_assistant.html')

### Route for handling the login page logic ###
from users.user_verify import verify
from users.view_threads import view

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if 'signedUp' in request.args:
        signedUp = "New account created, please login again."
    else:
        signedUp = None

    if request.method == 'POST':
        if request.form['username'].strip() == "" or request.form['password'].strip() == "":
            error = 'Please enter Username/Password.'
        else:
            if verify(request.form['username'], request.form['password']) == False:
                error = 'Invalid Credentials. Please try again.'
            else:
                session['username'] = request.form['username']
                if len(view(session['username'])) == 0:
                    return redirect(url_for('create_assistant'))
                else:
                    return redirect(url_for('chat'))
    return render_template('login.html', error=error, signedUp=signedUp)

### Route for handling the sign up page logic ###
from users.user_new import verify
from users.user_new import append
from moderation import check

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    error = None
    if request.method == 'POST':
        if request.form['username'].strip() == "" or request.form['password'].strip() == "":
            error = 'Please enter Username/Password.'
        else:
            moderation = check(request.form['username'])
            if  moderation is False:
                if verify(request.form['username']) is True:
                    error = 'Username already taken.'
                else:
                    if len(request.form['password']) <   5:
                        error = 'Password too short.\n Needs to be ≥ 5 characters.'
                    else:
                        append(request.form['username'], request.form['password'])
                        error = None
                        signedUp = True
                        return redirect(url_for('login', signedUp=signedUp))
            else:
                error = moderation
    return render_template('sign_up.html', error=error)

### Routes for handling the index and logout functionality ###
@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

# Running the app
if __name__ == '__main__':
    # Only use below in dev server.
    app.config["DEBUG"] = True
    app.run(host="127.0.0.1", port=5000)

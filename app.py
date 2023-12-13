from flask import Flask, render_template, redirect, url_for, request, session
import flask
from flask_session import Session

app = flask.Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Route for all logic in chat
@app.route('/chat/', methods=['GET', 'POST'])
def chat():
    from users.view_threads import view
    from thread.display_thread import display
    from moderation import check
    from thread.message import create as message_create
    from assistant.run_assistant import create as run_create
    from assistant.run_assistant import status

    threads = view(session["username"])
    error = ""

    exempt = ["My target grade is a any. Respond, in a short response. But only using the A-Level OCR curriculum. Your responses should be a sentence or two, unless the user’s request requires reasoning or long-form outputs. Only write the response, no pleasantries."]

    if 'thread' in request.args:
        thread_id = str(request.args['thread'])
    else:
        thread_id = threads[0]

    response = display(thread_id)

    if request.method == 'POST':
        query_type = request.form.get('query_type')
        query = request.form['query']
        if query_type != None and query.strip() != "":
            moderation = check(query)
            if moderation is False:
                message_create(thread_id,query,query_type)
                if response[-1].run_id == None:
                    run_id = run_create(thread_id)
                else:
                    run_id = response[-1].run_id
                while status(thread_id, run_id) is False:
                    response = "typing..."
                return redirect(url_for("chat", thread=thread_id))
            else:
                response = moderation
    
    return render_template('chat.html', exempt=exempt, response=response, error=error, username=session["username"], threads=threads, num_threads=len(threads))

# Route for all logic when making new thread
@app.route('/create_thread', methods=['GET', 'POST'])
def create_thread():
    from thread.create_thread import create
    from users.append_thread import append
    if request.method == 'POST':
        grade = request.form.get('grades')
        file = request.form.get('fileInput')
        if grade != None:
            thread = create(grade, file)
            append(session["username"], thread)
            return redirect(url_for('chat'))
    return render_template('create_thread.html')

# Route for all logic once logged in
@app.route('/create_assistant', methods=['GET', 'POST'])
def create_assistant():
    from assistant.create_assistant import create
    from users.append_assistant import append
    if request.method == 'POST':
        language = request.form['language']
        user_type = request.form.get('userTypeToggle')
        assistant = create(session["username"], language, user_type)
        append(session["username"], assistant=assistant.id)
        return redirect(url_for('create_thread'))
    return render_template('create_assistant.html')

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    from users.user_verify import verify
    from users.view_threads import view
    error = None
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
    return render_template('login.html', error=error)

# Route for handling the sign up page logic
@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    from users.user_new import verify
    from users.user_new import append
    from moderation import check
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
                        return redirect(url_for('login'))
            else:
                error = moderation
    return render_template('sign_up.html', error=error)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

if __name__ == '__main__':
    # Only use below in dev server. 
    app.config["DEBUG"] = True
    app.run(host="127.0.0.1", port=5000)
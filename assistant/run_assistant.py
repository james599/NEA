def create(thread_id):

    user_db = open("users/users.txt", "r")
    db = user_db.readlines()
    user_db.close()
    for user_record in db:
        if thread_id in user_record:
            assistant_id = user_record.split(",")[3].split("|")[0]

    from openai import OpenAI
    import os
    client = OpenAI(os.environ["OPENAI_KEY"])

    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id,
    )

    return run.id

def status(thread_id, run_id):
    from openai import OpenAI
    import os
    client = OpenAI(os.environ["OPENAI_KEY"])

    run = client.beta.threads.runs.retrieve(
        thread_id=thread_id,
        run_id=run_id
    )

    if run.status == "completed":
        return True
    else:
        return False
     

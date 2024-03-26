from openai import OpenAI
import os
def create(thread_id: str) -> str:
    user_db = open("users/users.txt", "r")
    db = user_db.readlines()
    user_db.close()
    for user_record in db:
        if thread_id in user_record:
            assistant_id = user_record.split(",")[3].split("|")[0]
            
    client = OpenAI(os.environ["OPENAI_KEY"])

    # Create run of a thread
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id,
    )

    return run.id

def status(thread_id: str, run_id: str) -> bool:
    client = OpenAI(os.environ["OPENAI_KEY"])

    # Checks status of run of a thread
    run = client.beta.threads.runs.retrieve(
        thread_id=thread_id,
        run_id=run_id
    )

    if run.status == "completed":
        return True
    return False
     

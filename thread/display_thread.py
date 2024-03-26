from openai import OpenAI
import os
def display(thread_id: str) -> array:
    client = OpenAI(os.environ["OPENAI_KEY"])

    # Retrieve all messages associated with the specified thread
    messages = client.beta.threads.messages.list(
        thread_id=thread_id
    )

    return messages.data

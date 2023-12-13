def display(thread_id):

    from openai import OpenAI
    import os
    client = OpenAI(os.environ["OPENAI_KEY"])

    messages = client.beta.threads.messages.list(
        thread_id=thread_id
    )

    return messages.data

def display(thread_id):

    from openai import OpenAI
    client = OpenAI(api_key = "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")

    messages = client.beta.threads.messages.list(
        thread_id=thread_id
    )

    return messages.data
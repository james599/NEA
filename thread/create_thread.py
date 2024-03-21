def create(grade, file):
    from openai import OpenAI
    import os
    client = OpenAI(os.environ["OPENAI_KEY"])

    thread = client.beta.threads.create()

    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=f"My target grade is a {grade}. Respond, in a short response. But only using the A-Level OCR curriculum. Your responses should be a sentence or two, unless the user’s request requires reasoning or long-form outputs. Only write the response, no pleasantries."
    )
    
    if file is not None:
        # TODO: Add regex on file
        uploaded_file = client.files.create(
            file=open(file, "rb"),
            purpose="assistants"
        ) # adding file to openai servers

        client.beta.assistants.files.create(
            assistant_id=message.assistant_id, 
            # retrieving assistant_id using json response from message 
            file_id=uploaded_file.id
        ) # adding file data to assistant model

    return thread.id

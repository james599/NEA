from openai import OpenAI
import os
def create(grade: str, file: bytes) -> str:
    # Initialize the OpenAI API client
    client = OpenAI(os.environ["OPENAI_KEY"])
    # Create a new thread
    thread = client.beta.threads.create()
    # Create a new message with the specified content
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        # Personalised context
        content=f"My target grade is a {grade}. Respond, in a short response. But only using the A-Level OCR curriculum. Your responses should be a sentence or two, unless the user’s request requires reasoning or long-form outputs. Only write the response, no pleasantries."
    )
    
    if file is not None:
        # TODO: Add regex on file
        # Upload the file to the OpenAI API server
        uploaded_file = client.files.create(
            file=open(file, "rb"),
            purpose="assistants"
        )

        # Create a new connection between the assistant and the uploaded file/image
        # To add file data to assistant model
        client.beta.assistants.files.create(
            assistant_id=message.assistant_id,  # id of assistant model
            file_id=uploaded_file.id
        )

    return thread.id

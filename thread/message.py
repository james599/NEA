def create(thread_id, query, query_type):
    from openai import OpenAI
    import os
    client = OpenAI(os.environ["OPENAI_KEY"])

    try:
        if query_type == "Exam":   # Exam Question
            client.beta.threads.messages.create(
                thread_id=thread_id,
                role="user",
                content= f"Can you act as an examiner, setting a single A-level OCR exam question only from the A-level OCR curriculum. Make a one of a choice between: definition, describe, using example, explain questions showing the number of marks they should be. Then display a brief mark scheme. For context: {query}"
            )
        elif query_type == "QA":   # Question Answering
            client.beta.threads.messages.create(
                thread_id=thread_id,
                role="user",
                content= f"Can you act as a textbook/teacher trying to answer my question, in a very short response, using a real-life example where applicable. But only using the A-Level OCR curriculum. For context: {query}"
            )
        return True
    except:
        return "ERROR: ChatGPT unreachable. Contact creator"

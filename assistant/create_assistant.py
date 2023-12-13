def create(username, language, user_type):
    from openai import OpenAI
    import os
    client = OpenAI(os.environ["OPENAI_KEY"])

    if user_type is not None: # Teacher
        assistant = client.beta.assistants.create(
            instructions=f'''You are assisting me, A-Level Computer Science teacher, who will ask two types of questions:
                            1. Question Answering - specific knowledge based questions so I can teach an A-Level class include breif summaries of anacdotes/examples
                            2. Create Exam Questions - give me example exam questions based closely on the question/context I give you
                            please answer in {language}''',
            name=username,
            tools=[{"type": "code_interpreter"}, {"type": "retrieval"}],
            model="gpt-3.5-turbo",
        )

    elif user_type is None: # Student
        assistant = client.beta.assistants.create(
            instructions=f'''You are assisting me, A-Level Computer Science student, who will ask two types of questions:
                            1. Question Answering - specific knowledge based questions so I can understand the A-Level curriculum
                            2. Create Exam Questions - give me example exam questions based closely on the question/context I give you
                            please answer in {language}''',
            name=username,
            tools=[{"type": "code_interpreter"}],
            model="gpt-3.5-turbo",
        )

    return assistant

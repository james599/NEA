def check(query):
    from openai import OpenAI
    import os
    client = OpenAI(os.environ["OPENAI_KEY"])

    if client.moderations.create(input=query, model="text-moderation-latest").results[0].flagged == True:
        return "Please don't enter this type of content into this AI."
    return False

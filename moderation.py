def check(query):
    from openai import OpenAI
    import os
    
    # Initialize the OpenAI client with the provided OpenAI API key
    client = OpenAI(os.environ["OPENAI_KEY"])

    # Check if the input query is flagged by the OpenAI latest model
    if client.moderations.create(input=query, model="text-moderation-latest").results[0].flagged == True:
        return "Please don't enter this type of content into this AI."
    # Return False if the input query passes moderation
    return False

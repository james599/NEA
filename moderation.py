def check(query):
    from openai import OpenAI
    client = OpenAI(api_key = "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")

    if client.moderations.create(input=query, model="text-moderation-latest").results[0].flagged == True:
        return "Please don't enter this type of content into this AI."
    return False
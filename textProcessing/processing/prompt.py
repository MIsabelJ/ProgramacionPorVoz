import openai
def traducir(instruccion):
    openai.api_key = "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"

    model_engine = "text-davinci-002"
    prompt = f"En python y sin agregados {instruccion}"
    completion = openai.Completion.create(engine=model_engine,
                                          prompt=prompt,
                                          max_tokens=1024,
                                          n=1,
                                          stop=None,
                                          temperature=0.7)

    for choice in completion.choices:
        print(f"Response {choice.text}")
    return choice.text
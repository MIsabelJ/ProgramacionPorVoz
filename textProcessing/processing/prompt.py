import openai
def traducir(instruccion):
    openai.api_key = "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"

    model_engine = "text-davinci-002"
    prompt = f"En python y sin agregados. Si lo siguiente no es algo relacionado con codigo dame como respuesta un mensaje que diga 'Error, no es relacionado con codigo': {instruccion}"
    completion = openai.Completion.create(engine=model_engine,
                                          prompt=prompt,
                                          max_tokens=1024,
                                          n=1,
                                          stop=None,
                                          temperature=0.7)

    for choice in completion.choices:
        print(f"Response {choice.text}")
    return choice.text
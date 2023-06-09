
import openai

def traducir(instruccion):
    openai.api_key = "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"

    model_engine = "text-davinci-002"
    prompt = f'En python y solo incluyendo cabecera. Si lo siguiente no es algo relacionado con codigo dame como respuesta un mensaje que diga "Error, no es relacionado con codigo": {instruccion}'
    
    completion = openai.Completion.create(engine=model_engine,
                                          prompt=prompt,
                                          max_tokens=1024,
                                          n=1,
                                          stop=None,
                                          temperature=0.7)

    for choice in completion.choices:
        print(f"Response {choice.text}")
    return choice.text
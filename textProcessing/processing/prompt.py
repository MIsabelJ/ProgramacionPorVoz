
import openai

def traducir(ruta, instruccion):
    openai.api_key = ""
    doc = ""
    with open (ruta, 'r') as f:
        doc = f.read()

    model_engine = "text-davinci-002"
    prompt = f'''
    Sobre lo siguiente: {doc}
    Vas a recibir una indicacion y necesito que te limites a darme solamente el codigo en python sin agregados: {instruccion}.
    '''
    completion = openai.Completion.create(engine=model_engine,
                                          prompt=prompt,
                                          max_tokens=1024,
                                          n=1,
                                          stop=None,
                                          temperature=0.7)

    for choice in completion.choices:
        print(f"Response {choice.text}")

    return choice.text

def escribir(ruta, instruccion):
    with open(ruta, 'w') as w:
         w.write(traducir (ruta, instruccion))


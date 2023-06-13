
import openai

def traducir(ruta, instruccion):
    openai.api_key = "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"
    with open (ruta, 'r') as f:
        doc = f.read()

    model_engine = "text-davinci-002"
    prompt = f'''Funcionas para traducir lenguaje natural a codigo de python.
    No tabulas lineas de codigo ya existentes y siempre que creas una linea nueva dejas un renglon libre abajo de dicha linea.
    Si lo siguiente no es algo relacionado con codigo dame como respuesta un mensaje que diga "Error, no es relacionado con codigo".
    El archivo que necesito modificar es el siguiente: {doc}. 
    Necesito que contenga el contenido ya existente en el archivo mas lo indicado en la siguiente instruccion: {instruccion}
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


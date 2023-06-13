
import openai

def traducir(instruccion):
    openai.api_key = "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"
    ruta = "../lectura-modificacion/archivo.py"
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

    if choice.text == "Error, no es relacionado con codigo.":
        return choice.text
    else:
        with open(ruta, 'w') as w:
            w.write(choice.text)
    return choice.text
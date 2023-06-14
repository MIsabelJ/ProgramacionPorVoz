
import openai

def traducir(ruta, instruccion):
    openai.api_key = "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"
    doc = ""
    with open (ruta, 'r') as f:
        doc = f.read()

    model_engine = "text-davinci-002"
    prompt = f'''
    A lo siguiente: {doc}
    Modificalo segun la siguiente instruccion: {instruccion}.
    Debe ser en leanguaje tipo python y si la instruccion es algo no relacionado a coduigo de python dame como respuesta "print("Error")"
    No se deben agregar lineas ni comillas que no sean codigo a la respuesta.
    '''
    completion = openai.Completion.create(engine=model_engine,
                                          prompt=prompt,
                                          max_tokens=1024,
                                          n=1,
                                          stop=None,
                                          temperature=0.7)

    #for choice in completion.choices:
    #    print(f"{choice.text}")
    
    print (completion.choices[0].text)

    return completion.choices[0].text

def escribir(ruta, instruccion):
    with open(ruta, 'w') as w:
         w.write(traducir (ruta, instruccion))


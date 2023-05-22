def crearVariable(instruccion, arrayIdentificadores):
    nombre = ""
    valor = ""

    #Palabras claves que anteceden al nombre de la variable
    indicadoresNombre = ["nombre", "llamada", "entera", "int", "string", "texto", "es", "sea"]
    indicadoresValor = [
        "valor",
        "número",
        "string",
        "cadena",
        "texto",
        "instrucción",
        "instrucciones",
        "entero",
    ]

    #Se encuentra el valor a asignar y se eliminan esas palabras de la instrucción
    #para que no interfieran con el análisis del nombre de la variable
    posicionValor = filtrar(indicadoresValor, instruccion)[1]
    for i in range(len(instruccion)):
        if i >= posicionValor:
            valor += instruccion[i] + " "
            instruccion[i] = ""

    #Se encuentra el nombre de la variable
    nombre = filtrar(indicadoresNombre, instruccion)[0]
    if nombre in arrayIdentificadores:
        print(f"La variable {nombre} ya existe")
    else:
        arrayIdentificadores.append(nombre)
        return nombre + " = " + valor

#filtra la instrucción para encontrar la palabra clave que antecede al valor esperado.
#Devuelve una tupla con la palabra clave y su posición en la instrucción.
def filtrar(indicadores, instruccion):
    for i in reversed(range(len(instruccion))):
        if instruccion[i] in indicadores:
            if i > 0 and instruccion[i-1] in indicadores and instruccion[i-2] in indicadores:
                return (instruccion[i], i)

            else:
                return (instruccion[i+1], (i+1))
            
#ejemplo = "crear una variable entera llamada gato que contenga el valor 8"
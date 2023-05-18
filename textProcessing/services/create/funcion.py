def crearFuncion(instruccion, arrayIdentificadores):
    nombre = ""
    parametros = ""

    #Palabras claves que anteceden al nombre de la función
    indicadoresNombre = ["nombre", "llamada", "es", "sea"]
    indicadoresParametros = [
        "valor",
        "numero",
        "string",
        "cadena",
        "texto",
        "instrucción",
        "instrucciones",
        "entero",
        "parámetro",
        "parámetros",
        "a"
    ]

    #Se encuentran los parámetros y se eliminan esas palabras de la instrucción
    #para que no interfieran con el análisis del nombre de la función
    posicionParametro = filtrar(indicadoresParametros, instruccion)[1]
    for i in range(len(instruccion)):
        if i >= posicionParametro:
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
                return (instruccion[i+1], (i+1))

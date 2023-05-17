def asignar(instruccion, arrayNombres):
    nombre = ""
    valor = ""

    #Palabras claves que anteceden a la variable buscada
    indicadoresNombre = ["nombre", "llamada", "variable", "a", "es"]
    indicadoresValor = [
        "valor",
        "numero",
        "string",
        "cadena",
        "texto",
        "instruccion",
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
    if nombre in arrayNombres:
        print(nombre, " = ", valor)
    else:
        print(f"La variable {nombre} no existe")

#filtra la instrucción para encontrar la palabra clave que antecede al valor esperado.
#Devuelve una tupla con la palabra clave y su posición en la instrucción.
def filtrar(indicadores, instruccion):
    for i in reversed(range(len(instruccion))):
        if instruccion[i] in indicadores:
            if i > 0 and instruccion[i-1] in indicadores and instruccion[i-2] in indicadores:
                return (instruccion[i], i)
            else:
                return (instruccion[i+1], (i+1))
    
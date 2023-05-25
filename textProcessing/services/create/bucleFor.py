def crearBucleFor(instruccion, arrayIdentificadores):
    elemento = ""
    lista = []

    #Palabras claves que anteceden al nombre de la función
    indicadoresElemento = ["nombre", "llamada", "llamado", "es", "sea", "cada", "elemento", "objeto", "valor", "variable"]
    indicadoresLista = [
        "string",
        "cadena",
        "texto",
        "variable",
        "lista",
        "arreglo",
        "array",
        "diccionario",
        "conjunto",
        "rango"
    ]

    #Se encuentran los parámetros y se eliminan esas palabras de la instrucción
    #para que no interfieran con el análisis del nombre de la función
    posicionLista = filtrar(indicadoresLista, instruccion)[1]
    for i in range(len(instruccion)):
        if i >= posicionLista and i < len(instruccion):
            lista.append(instruccion[i])
    del instruccion[posicionLista:]


    #Se encuentra el nombre del elemento del bucle
    elemento = filtrar(indicadoresElemento, instruccion)[0]
    if elemento == "none":
        elemento = "i"

    #Se analizan casos especiales como rangos y strings y se retorna el bucle for
    if "rango" in instruccion:
        contiene = False
        for palabra in ["del", "desde", "hasta", "al", "a", "principio", "inicio", "final"]:
            if (palabra in lista):
                contiene = True
                lista.remove(palabra)
        if contiene == False:
            return "for " + elemento + " in range(len("  + lista[0] + ")):"
        return "for " + elemento + " in range("  + lista[0] + ", " + lista[1] + "):"
    elif ("string" in instruccion or "cadena" in instruccion or "texto" in instruccion):
        return "for " + elemento + " in \"" + lista[0] + "\":"
    return "for " + elemento + " in " + lista[0] + ":"
    
#filtra la instrucción para encontrar la palabra clave que antecede al valor esperado.
#Devuelve una tupla con la palabra clave y su posición en la instrucción.
def filtrar(indicadores, instruccion):
    for i in reversed(range(len(instruccion))):
        if instruccion[i] in indicadores:
            if i > 0 and instruccion[i-1] in indicadores and instruccion[i-2] in indicadores:
                return (instruccion[i], i)
            else:
                return (instruccion[i+1], (i+1))
    return ("none", -1)

# ejemplo = "crear un bucle for para iterar sobre cada elemento persona en la lista personas"
# ejemplo = "crear un bucle for para recorrer los valores numéricos del rango del 1 al 10"
# ejemplo = "crear un bucle for para recorrer los valores numéricos del rango de la lista perro"
# ejemplo = "crear un bucle for para procesar cada caracter de la cadena de texto mensaje"
# ejemplo = "crear un bucle for para iterar sobre cada clave en el diccionario datos"
# ejemplo = "crear un bucle for para examinar cada elemento producto en la lista inventario"
# ejemplo = "crear un bucle for para recorrer cada día de la semana en la lista dias_semana"
# ejemplo = "crear un bucle for para calcular el cuadrado de cada número en la lista numero"
# ejemplo = "crear un bucle for para iterar sobre cada elemento estudiante en la lista estudiantes"
# ejemplo = "crear un bucle for para procesar cada valor booleano en la lista valores"
# ejemplo = "crear un bucle for para recorrer cada mes del año en la lista meses"
# valor = crearBucleFor(ejemplo.split(" "), ["numero", "perro", "edad", "nombre", "cantidad", "llamada"])
# print(valor)
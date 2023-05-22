def crearLista(instruccion, arrayIdentificadores):
    nombre = ""
    valores = []

    #Palabras claves que anteceden al nombre de la variable
    indicadoresNombre = ["nombre", "llamada", "es", "sea"]
    indicadoresValores = [
        "número",
        "números",
        "string",
        "strings",
        "cadena",
        "cadenas",
        "texto",
        "valor",
        "valores",
        "contenga"
    ]

    #Se encuentran los parámetros y se eliminan esas palabras de la instrucción
    #para que no interfieran con el análisis del nombre de la función
    posicionParametro = filtrar(indicadoresValores, instruccion)[1]
    for i in range(len(instruccion)):
        if i >= posicionParametro and i < len(instruccion):
            #si y está en la instrucción, es la penúltima letra y no es el valor actual, lo agregamos a la lista de parámetros
            if "y" in instruccion and "y" == instruccion[len(instruccion)-2] and "y" != instruccion[i]:
                valores.append(instruccion[i])
            #sino, si e está en la instrucción, es la penúltima letra y no es el valor actual, agregamos al valor considerando a e
            elif "e" in instruccion and "e" == instruccion[len(instruccion)-2]  and "e" != instruccion[i]:
                valores.append(instruccion[i])
    del instruccion[posicionParametro:]

    #Se encuentra el nombre de la funcion
    nombre = filtrar(indicadoresNombre, instruccion)[0]
    if nombre in arrayIdentificadores:
        print(f"La funcion {nombre} ya existe")
    else:
        arrayIdentificadores.append(nombre)
        values = ""
        for valor in valores:
            if valor == valores[len(valores)-1]:
                values += valor
            else: values += valor + ", "
        return nombre + " = [" + values +"]"

#filtra la instrucción para encontrar la palabra clave que antecede al valor esperado.
#Devuelve una tupla con la palabra clave y su posición en la instrucción.
def filtrar(indicadores, instruccion):
    for i in reversed(range(len(instruccion))):
        if instruccion[i] in indicadores:
            if i > 0 and instruccion[i-1] in indicadores and instruccion[i-2] in indicadores:
                return (instruccion[i], i)
            elif instruccion[i-1] in indicadores:
                return (instruccion[i], i)
            else:
                return (instruccion[i+1], (i+1))

# ejemplo = "crear una lista llamada asdf que contenga los valores 8 9 10 11 12 13 14 15 16 17 y 18"
# valor = crearLista(ejemplo.split(" "), ["numero", "perro", "edad", "nombre", "cantidad", "llamada"])
# print(valor)
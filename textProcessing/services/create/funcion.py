def crearFuncion(instruccion, arrayIdentificadores):
    nombre = ""
    parametros = []

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
        "parámetros"
    ]

    #Se encuentran los parámetros y se eliminan esas palabras de la instrucción
    #para que no interfieran con el análisis del nombre de la función
    posicionParametro = filtrar(indicadoresParametros, instruccion)[1]
    for i in range(len(instruccion)):
        if i >= posicionParametro and i < len(instruccion):
            #si y está en la instrucción, es la penúltima letra y no es el valor actual, lo agregamos a la lista de parámetros
            if "y" in instruccion and "y" == instruccion[len(instruccion)-2] and "y" != instruccion[i]:
                parametros.append(instruccion[i])
            #sino, si e está en la instrucción, es la penúltima letra y no es el valor actual, agregamos al valor considerando a e
            elif "e" in instruccion and "e" == instruccion[len(instruccion)-2]  and "e" != instruccion[i]:
                parametros.append(instruccion[i])
    del instruccion[posicionParametro:]

    #Se encuentra el nombre de la funcion
    nombre = filtrar(indicadoresNombre, instruccion)[0]
    if nombre in arrayIdentificadores:
        print(f"La funcion {nombre} ya existe")
    else:
        arrayIdentificadores.append(nombre)
        params = ""
        for param in parametros:
            if param == parametros[len(parametros)-1]:
                params += param
            else: params += param + ", "
        return "def " + nombre + "(" + params +"):"

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

ejemplo = "crear una funcion cuyo nombre es sea que reciba como parámetros a b c e indice"
valor = crearFuncion(ejemplo.split(" "), ["numero", "perro", "edad", "nombre", "cantidad", "llamada"])
print(valor)
 
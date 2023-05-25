#Para probar, ejecutar este archivo desde la consola con el 
#comando: python assignBranch.py descomentando los ejemplos, el array 
#de nombres y la llamada a la funcion asignar que están al final


def asignar(instruccion, arrayIdentificadores):
    nombre = ""
    valor = ""

    #Palabras claves que anteceden a la variable buscada
    indicadoresNombre = ["nombre", "llamada", "variable", "a", "es"]
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
            elif instruccion[i-1] in indicadores:
                return (instruccion[i], i)
            else:
                return (instruccion[i+1], (i+1))
    
# arrayIdentificadores = ["numero", "perro", "edad", "nombre", "cantidad", "llamada"]
# ejemplo = "asignar a la variable cuyo nombre es nombre el valor metodología de la investigación es piola"
# ejemplo = "asignar a la variable numero el valor 8"
# ejemplo = "asignar a la variable llamada nombre el valor 8"
# ejemplo = "asignar a la variable cuyo nombre es numero el valor 8"
# ejemplo = "asignar a numero el valor 8"
# ejemplo = "asignar a la variable de nombre numero el valor 8"
# asignar(ejemplo.split(" "), arrayIdentificadores)
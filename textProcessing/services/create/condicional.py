from asyncio.windows_events import NULL
from sre_constants import RANGE


def crearCondicional(instruccion):
    # Lista de palabras que va a anteceder la condicion
    identificadores = ["condicion","sea","si","verifique"]
    condicion = []
    # Desglose de la instruccion en donde obtenemos el indice en el que empieza la condicion
    for i in range(len(instruccion)):
        if instruccion[i] in identificadores:
            indice = i+1
            break
        indice = NULL

    # Verificamos si se encontro la palabra clave y se lo asignamos al arrayCondicion
    if indice == NULL:
        print("Error, no se encuentra indice")
    else:
        for i in range(indice, len(instruccion) ):
            condicion.append(instruccion[i])
            
    # Recorremos la instruccion y eliminamos posibles palabras sobrantes
    palabrasSobrantes =["sean","sea","que","y"]
    for i in reversed(range(len(condicion))):
        if condicion[i] in palabrasSobrantes:
            condicion.remove(condicion[i])
        if condicion[i] == "mayor":
            condicion[i] = ">"
        if condicion[i] == "menor":
            condicion[i] = "<"
        if condicion[i] == "igual" or condicion[i] == "iguales":
            condicion[i] = "=="

    sentenciaFinal =""
    for i in range(len(condicion)):
        if condicion[i] == "<" or condicion[i] == ">" or condicion[i] == "==":
            condicion[i], condicion[1] = condicion[1], condicion[i]
    
    for i in range(len(condicion)):
        sentenciaFinal = f"{sentenciaFinal} {condicion[i]}"
    
    sentenciaFinal = f"if {sentenciaFinal}:"
    return sentenciaFinal
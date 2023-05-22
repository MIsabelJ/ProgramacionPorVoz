from . import variable as variable
from . import funcion as funcion
from . import comentario as comentario

def crear(instruccion, arrayIdentificadores):
    indicadoresElementos = [
        "bucle",
        "variable",
        "funcion",
        "metodo",
        "lista",
        "arreglo",
        "array",
        "for",
        "para",
        "while",
        "mientras",
        "condicional",
        "if",
        "comentario",
        "mensaje",
        "print",
        "imprimir"
    ]

    for palabra in instruccion:
        if palabra == "variable":
            retorno = variable.crearVariable(instruccion, arrayIdentificadores)
            print(retorno)
            break
        if palabra in ["funcion", "metodo"]:
            retorno = funcion.crearFuncion(instruccion, arrayIdentificadores)
            break
        if palabra in ["lista", "arreglo", "array"]:
            print("Se ha creado una lista")
            break
        if palabra in ["for","para"]:
            print("Se ha creado un for")
            break
        if palabra in ["while", "mientras"]:
            print("Se ha creado un while")
            break
        if palabra in ["condicional", "if"]:
            print("Se ha creado un if")
            break
        if palabra == "comentario":
            print("Se ha creado un comentario")
            retorno = comentario.recibirMensaje(instruccion)
            break
        if palabra in ["mensaje", "print", "imprimir"]:
            print("Se ha creado un mensaje")
            break
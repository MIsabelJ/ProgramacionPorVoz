from . import variable as variable
from . import funcion as funcion
from . import comentario as comentario
from . import lista as lista
from . import bucleFor as bucleFor
from . import condicional as condicional
from . import bucleWhile as bucleWhile
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
            retorno = lista.crearLista(instruccion, arrayIdentificadores)
            break
        if palabra in ["for","para"]:
            retorno = bucleFor.crearBucleFor(instruccion, arrayIdentificadores)
            print(retorno)
            break
        if palabra in ["while", "mientras"]:
            print("Se ha creado un while")
            retorno = bucleWhile.crearBucleWhile(instruccion)
            break
        if palabra in ["condicional", "if"]:
            retorno = condicional.crearCondicional(instruccion)
            print("Se ha creado un if")
            print(retorno)
            break
        if palabra == "comentario":
            print("Se ha creado un comentario")
            retorno = comentario.recibirMensaje(instruccion)
            print(retorno)
            break
        if palabra == "comentar":
            print("Se ha comentado una línea")
            break
        if palabra in ["mensaje", "print", "imprimir"]:
            print("Se ha creado un mensaje")
            break
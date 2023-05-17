def crear(palabraDividida):
    indicadoresElemetos = [
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

    for palabra in palabraDividida:
        if palabra == "variable":
            palabraDividida.remove("variable")
            print("Se ha creado una variable")
            break
        if palabra in ["funcion", "metodo"]:
            palabraDividida.remove(palabra)
            print("Se ha creado una funcion")
            break
        if palabra in ["lista", "arreglo", "array"]:
            palabraDividida.remove(palabra)
            print("Se ha creado una lista")
            break
        if palabra in ["for","para"]:
            palabraDividida.remove(palabra)
            print("Se ha creado un for")
            break
        if palabra in ["while", "mientras"]:
            palabraDividida.remove(palabra)
            print("Se ha creado un while")
            break
        if palabra in ["condicional", "if"]:
            palabraDividida.remove(palabra)
            print("Se ha creado un if")
            break
        if palabra == "comentario":
            palabraDividida.remove(palabra)
            print("Se ha creado un comentario")
            break
        if palabra in ["mensaje", "print", "imprimir"]:
            palabraDividida.remove(palabra)
            print("Se ha creado un mensaje")
            break
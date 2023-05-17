def asignar(palabraDividida, arrayNombres):
    nombre = ""
    valor = ""

    indicadoresNombre = ["nombre", "llamada", "variable", "a", "es"]
    indicadoresValor = [
        "valor",
        "de",
        "numero",
        "string",
        "cadena",
        "texto",
        "palabra",
        "palabras",
        "entero",
    ]

    nombre = filtrar(indicadoresNombre, palabraDividida)
    if nombre in arrayNombres:
        valor = filtrar(indicadoresValor, palabraDividida)
        print(nombre, " = ", valor)
    else:
        print(f"La variable {nombre} no existe")
 

def filtrar(indicadores, palabraDividida):
    for i in reversed(range(len(palabraDividida))):
        if palabraDividida[i] in indicadores:
            if i > 0 and palabraDividida[i-1] in indicadores:
                return palabraDividida[i]
            else:
                return palabraDividida[i+1]  # Añadir +2 para obtener el valor en lugar del índice i+1

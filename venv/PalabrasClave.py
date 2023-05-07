from ReconocimientoDeAudio import grabarAudio

# Lista de palabras clave, por jerarquía.
palabrasClave = {
    # categoria : listaPalabrasClave
    "Nivel 1": ["crear", "llamar", "posición", "eliminar", "mover", "asignar", "comentar"], # "palabraClave"
    "Nivel 2": ["comentario", "bucle", "condicional", "función", "variable", "procedimiento", "mensaje"],
    "Nivel 3": ["llamado", "llamada", "nombre", "valor", "parámetro", "parámetros", "condición", "condiciones", "for", "if",
               "while", "do while", "int", "string", "float", "double", "char", "línea", "sección", "diga", "lea"]
}

# Función que busca las palabras clave en la lista pasada como parámetro, y devuelve las palabras clave encontradas en
# la lista, junto con la categoría a la que pertenecen.
def buscarPalabras(lista):
    for categoria, listaPalabrasClave in palabrasClave.items():
        for palabraClave in listaPalabrasClave:
            if palabraClave in lista:
                return categoria, palabraClave
    return None, None

# Buscamos coincidencias en la lista de strings que se reconoció por audio.
listaPalabras = grabarAudio() # Importo la lista.

resultado = {} # Acá se van a guardar las palabras que coincidieron.

for palabra in listaPalabras:
    categoria, palabraClave = buscarPalabras(palabra)
    if categoria not in resultado:
        resultado[categoria] = []
    resultado[categoria].append(palabraClave) # Agrego al final de la lista (append).

# Imprime los resultados.
for categoria, listaPalabrasClave in resultado.items():
    # Filtrar los valores None.
    listaPalabrasClave = list(filter(None, listaPalabrasClave))
    # ^ Hago esto porque saltaba un error al salir "none" en alguna lista.
    if listaPalabrasClave:
        print(f"{categoria}: {', '.join(listaPalabrasClave)}")
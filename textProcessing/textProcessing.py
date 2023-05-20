import services.index as index
# from anytree import Node

# crear = Node("crear")
# llamar = Node("llamar")
# eliminar = Node("eliminar")
# asignar = Node("asignar")
# comentar = Node("comentar")
# mover = Node("mover")
# insertar = Node("insertar")

# nodosPadre = [crear, llamar, eliminar, asignar, comentar, mover, insertar]
arrayIdentificadores = ["numero", "perro", "edad", "nombre", "cantidad", "llamada"]

# ejemplo = "crear un bucle for para iterar sobre cada elemento persona en la lista personas"
# ejemplo = "crear un bucle for para recorrer los valores numéricos del rango del 1 al 10"
palabraDividida = ejemplo.split(" ")
index.abrirNodo(palabraDividida, arrayIdentificadores)

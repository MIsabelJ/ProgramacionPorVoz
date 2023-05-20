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

ejemplo = "crear una funcion cuyo nombre es maullar que reciba como parámetros a b c e indice"

palabraDividida = ejemplo.split(" ")
index.abrirNodo(palabraDividida, arrayIdentificadores)

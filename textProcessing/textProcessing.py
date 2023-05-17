import services.index as index
from anytree import Node

crear = Node("crear")
llamar = Node("llamar")
eliminar = Node("eliminar")
asignar = Node("asignar")
comentar = Node("comentar")
mover = Node("mover")
insertar = Node("insertar")

nodosPadre = [crear, llamar, eliminar, asignar, comentar, mover, insertar]
arrayNombres = ["numero", "perro", "edad", "nombre", "cantidad", "llamada"]

ejemplo = "crear una variable que contenga el valor 8"

palabraDividida = ejemplo.split(" ")
index.abrirNodo(palabraDividida, arrayNombres)


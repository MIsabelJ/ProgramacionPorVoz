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

# ejemplo = "asignar a la variable numero el valor 8"
ejemplo = "asignar a la variable cuyo nombre es perro el valor agus"
# ejemplo = "asignar a la variable llamada número el valor 8"
# ejemplo = "asignar a la variable cuyo nombre es número el valor 8"
# ejemplo = "asignar a número el valor 8"
# ejemplo = "asignar a la variable de nombre número el valor 8"

palabraDividida = ejemplo.split(" ")
index.abrirNodo(palabraDividida, arrayNombres)

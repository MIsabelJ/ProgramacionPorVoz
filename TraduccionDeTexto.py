from os import name
import anytree
from anytree import Node, RenderTree

#Funcion para asignar
def ramaAsignar():
    #Se crea la variable que va a alojar la instrucción de manera global
    global salida

    #Recorremos la el array para extraer el nombre de la variable
    for i in range(len(array)):
        if (array[i] == "nombre"):
            nombre = array[i+1]

    #Recorremos la el array para extraer el valor de la variable
    for i in range(len(array)):
        if(array[i] == "valor"):
            valor = array[i+1]

    #Comprobamos que la variable exista y asignamos el prompt en la variable salida
    for i in arrayVariables:
        if(nombre == i):
            print("Variable encontrada!")
            salida = f"{nombre} = {valor}"
            return salida
        else:
            print("No se ha creado esa variable")
            salida = "error"
            return salida

#Funcion para crear
def ramaCrear():
     #Se crea la variable que va a alojar la instrucción de manera global
     global salida

     #Creamos los nodos hijos de "Crear"
     variable = Node("variable", parent=crear)
     bucle = Node("bucle", parent=crear)
     condicional = Node("condicional", parent=crear)
     comentario = Node("comentario", parent=crear)
     mensaje = Node("mensaje", parent=crear)
     arreglo = Node("arreglo", parent = crear)
     ingreso = Node("ingreso", parent = crear)
     
     #Recorremos el array verificando en qué nodo hijo entrar
     for i in array:
         #Nodo variable
         if(i == variable.name):
             for j in range(len(array)):
                 if(array[j] == "nombre"):
                     nombre = array[j+1]
                 if(array[j] == "valor"):
                     valor = array[j+1]
                 if(array[j] == "tipo"):
                     tipo = array[j+1]
             if(tipo == "cadena" or tipo == "caracter"):
                 salida = f'{nombre} = "{valor}"'
             else:
                 salida = f"{nombre} = {valor}"
         #Nodo bucle
         if(i == bucle.name):
             for j in range(len(array)):
                 #Bucle for
                 if(array[j] == "for" or array[j] == "para"):
                     tipo = "for"
                     for k in range(len(array)):
                         if(array[k] == "desde" and array[k+2] == "hasta"):
                             x = array[k+1]
                             y = array[k+3]
                         if(array[k] == "incremento"):
                             incremento = array[k+1]

                     #Asignamos el prompt en la variable salida
                     salida = f"for i in range({x},{y},{incremento}):"
                     break

                 #Blucle while
                 elif(array[j] == "while" or array[j] == "mientras"):
                     tipo = "while"
                     salida = f"{tipo}"
                     for k in range(len(array)):
                         condicion = f" " 
                         salida = f"{tipo} {condicion}"
                     break
             
                 
                  

     
     return salida

         

   

ejemplo = "asignar a la variable con el nombre numero el valor 10"
array = ejemplo.split(" ")
arrayVariables = ["numero", "edad", "cantidad", "sueldo"]

crear = Node("crear")
llamar = Node("llamar")
eliminar = Node("eliminar")
asignar = Node("asignar")
comentar = Node("comentar")
mover = Node("mover")
insertar = Node("insertar")

nodosPadre= [crear, llamar, eliminar, asignar, comentar, mover, insertar]

for i in array:
    if(i == "asignar"):
        ramaAsignar()
        break 
    if(i == "crear"):
        ramaCrear()
    

print(salida)
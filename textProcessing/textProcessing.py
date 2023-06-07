import services.index as index

arrayIdentificadores = ["numero", "perro", "edad", "nombre", "cantidad", "llamada"]



# ejemplo = "crear una funcion cuyo nombre es maullar que reciba como parámetro un String "
# ejemplo = "crear un comentario cuyo mensaje diga diga hola como estas"
# ejemplo = "crear un bucle for para iterar sobre cada elemento persona en la lista personas"
# ejemplo = "crear un bucle for para recorrer los valores numéricos del rango del 1 al 10"
# ejemplo = "crear un condicional while que tenga como condicion que a y b sean iguales "
ejemplo = "crear un bucle while que tenga como condicion que las variables a y b sean iguales"
palabraDividida = ejemplo.split(" ")
index.abrirNodo(palabraDividida, arrayIdentificadores)

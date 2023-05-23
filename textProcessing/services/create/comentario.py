#indicador comentario


#Molde indicacion: Crear un comentario que [palabra clave]...
#Molde indicacion: Crear un comentario de un mensaje que [palabra clave]...
def recibirMensaje(instruccion):
        indicadoresComentarios = ["diga","ponga","sea","exprese","comente"]
        comentario = ""
        for i in reversed(range(len(instruccion))):
            if instruccion[i] in indicadoresComentarios:

                    indice = i+1
                    break
        
        for i in range(indice, len(instruccion)):
            comentario = f"{comentario} {instruccion[i]}"
        print(comentario)
        return comentario



#ejemplo = "crear un mensaje que diga esta funcion es para crear"
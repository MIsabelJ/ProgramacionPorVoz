#indicador comentario



def recibirMensaje(instruccion):
        indicadoresComentarios = ["diga","comentar","mensaje","ponga"]
        comentario = ""
        i = len(instruccion)
        while i >= 0:
            if instruccion[i] in indicadoresComentarios:
                if instruccion[i-1] == instruccion[i]:
                    comentario = f"{comentario} {instruccion[i]}"
                    instruccion.remove(instruccion[i+1])
                    print("flag 1")
                    if i < len(instruccion):
                        print("flag 1.1")
                        i = i+1
                else:
                    comentario = f"{comentario} {instruccion[i+1]}"
                    instruccion.remove(instruccion[i+1])
                    print("flag 2")
                    if i < len(instruccion):
                        print("flag 2.1")
                        i = i+1
            i = i-1

        print(comentario)
        return comentario



#ejemplo = "crear comentario que diga esta funcion es para crear
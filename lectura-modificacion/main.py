filename = 'archivo.py'

cadena = "numero = 5\n"
cadena2 = "segundo = 3\n"
cadena3 = "print('suma: ', numero+segundo)\n"
cadena4 = """
if numero > segundo: 
    print("mayor")
else:
    print("menor")\n
"""
cadena5 = "segundo = 7\n"

class tab:
    def __init__(self, posicion, tipo):
        self.posicion = posicion
        self.tipo = tipo

# Crear un objeto
pos = 6
tipo = "if"
opciones = tab(pos-1,tipo)

cadena7 = "print('hola')\n"


#CREAR: Crea codigo de manera secuencial.
def crear(cadena):
    with open(filename, 'r+') as doc:
        contenido = doc.read()
        if contenido == '':
            doc.write(cadena)
            doc.write('\n')
        else:
            with open(filename,'a') as doc:
                doc.write(cadena)

#INSERTAR: Inserta codigo en la linea que desee el usuario.
def insertar(cadena,k):
    cadena = tabulado(cadena, opciones)
    with open(filename, 'r+') as doc:
        lineas = doc.readlines()
        lineas.insert(k, cadena)
        doc.seek(0)
        doc.writelines(lineas)

#ELIMINAR: Si la variable j es None elimina la linea guardada en la variable i, de lo contrario elimina la seccion de codigo de i a j.
def eliminar(i,j):
    with open(filename, 'r+') as doc:
        lineas = doc.readlines()
        if j is None: #ELIMINAR LINEA
            del lineas[i - 1]
        else: #ELIMINAR SECCION
            del lineas[i - 1:j]  #[i,j)
        doc.seek(0)
        doc.writelines(lineas)
        doc.truncate()


#COMENTAR: Si la variable j es None comenta la linea guardada en la variable i, de lo contrario comenta la seccion de codigo de i a j.
def comentar(i,j):
    with open(filename,'r+') as doc:
        lineas = doc.readlines()
        if j is None:
            lineas[i - 1] = "#" + lineas[i - 1] #COMENTAR LINEA
        else: #COMENTAR SECCION
            lineas.insert(i - 1, '"""\n')
            lineas.insert(j + 1, '"""\n')
        doc.seek(0)
        doc.writelines(lineas)

#ASIGNAR: Asigna o cambia de valor una variable
def asignar_valor(nombre,valor):
    with open(filename,'r+') as doc:
        lineas = doc.readlines()
        for i in range(len(lineas)):
            if lineas[i].startswith(nombre):
                lineas[i] = nombre + " = " + valor + "\n"
                break
        doc.seek(0)
        doc.writelines(lineas)

#MOVER DATOS: Mueve el codigo de la seccion i a j, a la linea k.
def mover_codigo(i,j,k):
    with open(filename,'r+') as doc:
        lineas = doc.readlines()
        datos_a_mover = lineas[i-1:j]
        del lineas[i-1:j]
        for iterador in range(0,j-i+1):
            aux = datos_a_mover[iterador]
            lineas.insert(k-1,aux)
            k += 1
        doc.seek(0)
        doc.writelines(lineas)

#TABULADO: Esta funcion es la que se encarga de establecer los tabulados del codigo dependiendo de donde se ingrese
def tabulado(cadena, opciones):
    if opciones.tipo == "": #si se quiere insertar dentro de una operacion entra
        return cadena
    else:
        with open(filename, 'r+') as doc:
            lineas = doc.readlines()
            for i in range(len(lineas)):
                if i == opciones.posicion and lineas[opciones.posicion]: #itera linea en linea hasta la posicion deseada
                    for j in range(opciones.posicion, 0, -1):
                        if j == opciones.posicion:
                            contador = ""
                            for caracter in lineas[j - 1]:
                                if caracter == " ":
                                    contador += " "
                                else:
                                    break
                            palabras = lineas[j - 1].split()
                            if palabras[0] == opciones.tipo:
                                cadena = "    " + contador + cadena  # agrego el tabulado + 4 espacios solo si me indica donde ponerlo
                                break
                            else:
                                cadena = contador + cadena
                                break
    return cadena




#crear(cadena5,opciones)


#crear(cadena)
#crear(cadena2)
#crear(cadena3)
#crear(cadena4,opciones)

#insertar(cadena7,opciones.posicion)

#eliminar_linea(3)
#eliminar_seccion(5,8)
#insertar(cadena5,1)
#comentar_linea(2)
#comentar_seccion(5,8)
#asignar_valor("segundo","10")
#mover_codigo(5,8,1)
#eliminar(5,7) #Eliminar Linea
#eliminar(4,None) #Eliminar Seccion
#comentar(1,None) #Comentar Linea
#comentar(4,7) #Comentar Seccion



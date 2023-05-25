import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

# Crear una ventana
ventana = tk.Tk()
estilo = ThemedStyle(ventana)
estilo.theme_use('default')

MontserratLight = './fonts/Montserrat/montserrat-Light.ttf'
MontserratRegular = './fonts/Montserrat/montserrat-Regular.ttf'
MontserratBold = './fonts/Montserrat/montserrat-Bold.ttf'
Consolas = './fonts/Consolas/consolas.ttf'

# Cargar la fuente
estilo.configure('.', font=('Montserrat', 12))

# Definir el tamaño de la ventana
ancho_ventana = 400
alto_ventana = 380
ventana.geometry(f"{ancho_ventana}x{alto_ventana}")
estilo.configure('.', font=(MontserratLight, 20))
ventana.configure(bg='white')



def borrar_placeholder(event):
    entry.delete(0, tk.END)
    entry.config(show='')

# Agregar elementos a la ventana 
titulo = ttk.Label(ventana, text="Cargar archivo")
subtitulo = ttk.Label(ventana, text="Selecciona un archivo de Python para comenzar")
entry = ttk.Entry(ventana)

entry.insert(0, 'Dirección del archivo')
entry.bind("<Button-1>", borrar_placeholder)
boton = ttk.Button(ventana, text="Seleccionar" )

titulo.pack()
subtitulo.pack()
entry.pack()
boton.pack()

# Iniciar el bucle de eventos de la interfaz gráfica
ventana.mainloop()
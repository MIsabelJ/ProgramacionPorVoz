import tkinter as tk
from ReconocimientoDeAudio import grabarAudio

#words_list = ""
def iniciarGrabacion():
    grabarAudio()


# Creo la ventana principal de la aplicación de escritorio
app = tk.Tk()

# Cambio el diseño de la ventana.
app.geometry("300x600")  # Dimensiones: ancho x alto
app.config(background="black")
tk.Wm.wm_title(app, "Programación por voz")

# Creo el botón que al presionarlo comienza a grabar la voz
grabar = tk.Button(app, text="Grabar", bg="white", width=10, height=2, font=("Verdana", 12), command=iniciarGrabacion)
#label = tk.Label(app, text="¡Hola, mundo!")
#label.pack()

grabar.pack()


app.mainloop()

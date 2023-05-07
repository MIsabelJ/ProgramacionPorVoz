import tkinter as tk
from ReconocimientoDeAudio import grabarAudio

def iniciarGrabacion():
    grabarAudio()


# Creo la ventana principal de la aplicación de escritorio
app = tk.Tk()

# Cambio el diseño de la ventana.
app.geometry("600x400")  # Dimensiones: ancho x alto
app.config(background="black")
tk.Wm.wm_title(app, "Programación por voz")

# Texto principal
texto = tk.Label(text="Presioná el botón para comenzar a grabar", bg="black", foreground="white", font=("Arial", 11))
texto.pack()

# Creo el botón que al presionarlo comienza a grabar la voz
grabar = tk.Button(app, text="Grabar", bg="white", width=10, height=2, font=("Verdana", 12), command=iniciarGrabacion)
grabar.pack()

app.mainloop()

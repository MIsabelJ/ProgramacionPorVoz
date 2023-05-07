import speech_recognition as sr
import pyaudio


def grabarAudio():
    # Configuración del reconocimiento de voz y micrófono
    r = sr.Recognizer()
    m = sr.Microphone()

    # Ajusta el micrófono al ruido de fondo
    with m as source:
        r.adjust_for_ambient_noise(source, duration=0.3)
    # Configuración de la entrada de audio
    print("Habla ahora:")
    with m as source:
        audio = r.listen(source)
    print("Procesando...")

    # Transformación del audio a texto
    try:
        texto = r.recognize_google(audio, language="es-ES")
        print("Dijiste: {}".format(texto))
        # Solicitar confirmación al usuario
        confirm = input("¿Es correcto? (s/n): ")
        if confirm.lower() == "s":
            # Desestructuro el texto en palabras y las guardo en una lista
            listaPalabras = texto.split()
            return listaPalabras
        else:
            print("Texto descartado.")
    except sr.UnknownValueError:
        print("No se ha podido reconocer lo que dijiste")
    except sr.RequestError as e:
        print("Error al solicitar los resultados del reconocimiento de voz; {0}".format(e))

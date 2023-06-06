import speech_recognition as sr
from queue import Queue
import threading

class Grabador:
    def __init__(self):
        self.texto = ""
        self.queue = Queue()
        self.interrupted = False
        self.r = sr.Recognizer()
        self.microfono = sr.Microphone()

    def run(self):
        self.recording_thread = threading.Thread(target=self._grabar_audio)
        self.recording_thread.start()

    def _grabar_audio(self):
        self.texto = ""
        # Iniciar la grabación de audio
        with self.microfono as source:
            self.r.adjust_for_ambient_noise(source)
            while not self.interrupted:
                audio_chunk = self.r.listen(source)
                self.queue.put(audio_chunk)

    def procesar_palabras(self):
        while True:
            audio_chunk = self.queue.get()
            try:
                if audio_chunk is None:
                    break
                self.texto += self.r.recognize_google(audio_chunk, language="es-ES") + " "
            except sr.UnknownValueError:
                ""

    def iniciar_procesamiento(self):
        self.procesamiento_thread = threading.Thread(target=self.procesar_palabras)
        self.procesamiento_thread.start()

    def detener_procesamiento(self):
        self.queue.empty()
        self.queue.put(None)  # Agregar marcador de finalización a la cola
        self.procesamiento_thread.join()

    def detener_grabacion(self):
        self.interrupted = True
        self.recording_thread.join()

from PyQt5 import QtWidgets, uic, QtCore

import threading
import sys
sys.path.append("..")
from textProcessing.processing.prompt import traducir
from reconocimientoVoz.reconocimientoAudio import Grabador
grabador = Grabador()
resultado = ""

qtCreatorFile=""
def startApp(ui_file):
    app = QtWidgets.QApplication(sys.argv)
    Ui_MainWindow, QtBaseClass = uic.loadUiType(ui_file)
    

    class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
        

        def __init__(self):
            QtWidgets.QMainWindow.__init__(self)
            Ui_MainWindow.__init__(self)
            self.setupUi(self)
            self.stackedWidget.setCurrentWidget(self.page)
            self.direccionArchivo = ""
            self.textoReconocido = ""
            self.textoProcesado = "" 
            ## ELEMENTOS
            # Pagina 1
            paginaUno = self.stackedWidget.widget(0)
            botonSeleccionar = paginaUno.findChild(QtWidgets.QPushButton, "botonSeleccionar")
            inputArchivo = paginaUno.findChild(QtWidgets.QLineEdit, "inputArchivo")

            # Pagina 2
            paginaDos = self.stackedWidget.widget(1)
            botonGrabar = paginaDos.findChild(QtWidgets.QPushButton, "botonGrabar")

            # Pagina 3
            paginaTres = self.stackedWidget.widget(2)
            inputMostrar = paginaTres.findChild(QtWidgets.QLineEdit, "inputMostrar_1")
            botonParar = paginaTres.findChild(QtWidgets.QPushButton, "botonParar")

            # Pagina 4
            paginaCuatro = self.stackedWidget.widget(3)
            inputMostrarFinal = paginaCuatro.findChild(QtWidgets.QLineEdit, "inputMostrarFinal")
            inputVistaPrevia = paginaCuatro.findChild(QtWidgets.QLineEdit, "inputVistaPrevia")
            botonAceptar = paginaCuatro.findChild(QtWidgets.QPushButton, "botonAceptar")
            botonReintentar = paginaCuatro.findChild(QtWidgets.QPushButton, "botonReintentar")

            ## EVENTOS

            if botonSeleccionar:
                botonSeleccionar.clicked.connect(lambda: self.archivoSeleccionado(inputArchivo))

            if botonGrabar:
                botonGrabar.clicked.connect(lambda: self.grabar(inputMostrar))

            if botonParar:
                botonParar.clicked.connect(lambda: self.parar(inputMostrarFinal, inputVistaPrevia))

            if botonAceptar:
                botonAceptar.clicked.connect(lambda: self.aceptar(inputMostrarFinal, inputVistaPrevia))

            if botonReintentar:
                botonReintentar.clicked.connect(lambda: self.reintentar(inputMostrar))
    
        # Página 1
        def archivoSeleccionado(self, inputArchivo):
            if inputArchivo.text() != "":
                self.direccionArchivo = inputArchivo.text()
                self.stackedWidget.setCurrentWidget(self.page_2)
        
        # Página 2
        def grabar(self, inputMostrar):
            self.stackedWidget.setCurrentWidget(self.page_3)
            grabador.run()
            grabador.iniciar_procesamiento()
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(lambda: self.verificar_cambios(inputMostrar))
            self.timer.start(100)  # Intervalo de verificación en milisegundos
            
        def verificar_cambios(self, inputMostrar):
            if grabador.texto != self.textoReconocido:
                self.textoReconocido = grabador.texto
                inputMostrar.setText(self.textoReconocido)

        # Página 3
        def parar(self, inputMostrarFinal, inputVistaPrevia):
            grabador.detener_procesamiento()
            grabador.detener_grabacion()
            self.textoProcesado = traducir(grabador.texto)
            #self.textoReconocido
            # acá enviamos el texto reconocido al Gabi y al Agus para que lo procesen
            # self.textoReconocido = "Hola mundo 33"
            self.timer.stop()
            self.stackedWidget.setCurrentWidget(self.page_4)
            inputMostrarFinal.setText(self.textoReconocido)
            inputVistaPrevia.setText(self.textoProcesado)

        # Página 4
        def aceptar(self, inputMostrarFinal, inputVistaPrevia):
            # Enviar dirección del archivo y texto reconocido al Franco para que lo inserte
            inputMostrarFinal.setText(grabador.texto)
            inputVistaPrevia.setText(resultado)
            print(self.direccionArchivo)

        def reintentar(self, inputMostrar):
            self.textoReconocido = ""
            self.textoProcesado = ""
            inputMostrar.setText("")
            self.grabador = Grabador()
            self.stackedWidget.setCurrentWidget(self.page_2)


    window = MyApp()
    window.show()
    sys.exit(app.exec_())


startApp("programacionPorVozDiseño.ui")
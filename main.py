import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "programacionPorVozDiseño.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    direccionArchivo = ""
    textoReconocido = ""
    textoProcesado = ""

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.stackedWidget.setCurrentWidget(self.page)

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
        botonParar = paginaTres.findChild(QtWidgets.QPushButton, "botonParar")

        # Pagina 4
        paginaCuatro = self.stackedWidget.widget(3)
        inputMostrar = paginaCuatro.findChild(QtWidgets.QLineEdit, "inputMostrar")
        inputVistaPrevia = paginaCuatro.findChild(QtWidgets.QLineEdit, "inputVistaPrevia")
        botonAceptar = paginaCuatro.findChild(QtWidgets.QPushButton, "botonAceptar")
        botonReintentar = paginaCuatro.findChild(QtWidgets.QPushButton, "botonReintentar")

        ## EVENTOS
        # Página 1
        def archivoSeleccionado():
            if inputArchivo.text() != "":
                self.direccionArchivo = inputArchivo.text()
                self.stackedWidget.setCurrentWidget(self.page_2)

        if botonSeleccionar:
            botonSeleccionar.clicked.connect(archivoSeleccionado)

        # Página 2
        def agregarDireccion():
            self.stackedWidget.setCurrentWidget(self.page_3)
            # iniciar función de reconocimiento de voz acá y guardarla en una variable

        if botonGrabar:
            botonGrabar.clicked.connect(agregarDireccion)

        # Página 3
        def parar():
            # detener la grabación dentro de este lugar
            self.textoProcesado = "hola Mundo"
            # asignarle el valor del texto reconocido
            # acá enviamos el texto reconocido al Gabi y al Agus para que lo procesen
            self.textoReconocido = "Hola mundo 33"
            self.stackedWidget.setCurrentWidget(self.page_4)
            inputMostrar.setText(self.textoReconocido)
            inputVistaPrevia.setText(self.textoProcesado)

        if botonParar:
            botonParar.clicked.connect(parar)

        # Página 4
        def aceptar():
            # Enviar dirección del archivo y texto reconocido al Franco para que lo inserte
            print(self.direccionArchivo)

        def reintentar():
            self.stackedWidget.setCurrentWidget(self.page_2)

        if botonAceptar:
            botonAceptar.clicked.connect(aceptar)

        if botonReintentar:
            botonReintentar.clicked.connect(reintentar)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

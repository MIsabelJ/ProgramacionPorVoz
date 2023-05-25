import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "programacionPorVozDiseño.ui" 

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

direccionArchivo = ""
textoReconocido =""
textoProcesado =""

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.stackedWidget.setCurrentWidget(self.page)
        ## PAGINAS
        # Pagina 1
        paginaUno = self.stackedWidget.widget(0)
        botonSeleccionar = paginaUno.findChild(QtWidgets.QPushButton, "botonSeleccionar")
        inputArchivo = paginaUno.findChild(QtWidgets.QLineEdit, "inputArchivo")

        def archivoSeleccionado():
            if inputArchivo.text() != "":
                self.stackedWidget.setCurrentWidget(self.page_2)
                setDireccionArchivo(inputArchivo.text())

        if botonSeleccionar:
            botonSeleccionar.clicked.connect(archivoSeleccionado)
            print(getDireccionArchivo())
            
        # Pagina 2
        paginaDos = self.stackedWidget.widget(1)
        botonGrabar = paginaDos.findChild(QtWidgets.QPushButton, "botonGrabar")

        def cambiar():
            self.stackedWidget.setCurrentWidget(self.page_3)
        
        if botonGrabar:
            botonGrabar.clicked.connect(cambiar)

        # Pagina 3
        paginaTres = self.stackedWidget.widget(2)
        botonParar = paginaTres.findChild(QtWidgets.QPushButton, "botonParar")

        #iniciar función de reconocimiento de voz acá y guardarla en una variable


        def parar():
            #detener la grabación dentro de este lugar
            # self.setTextoProcesado("hola Mundo") #asignarle el valor del texto reconocido
            #acá enviamos el texto reconocido al Gabi y al Agus para que lo procesen
            # self.setTextoReconocido("Hola mundo")
            self.stackedWidget.setCurrentWidget(self.page_4)
        
        if botonParar:
            botonParar.clicked.connect(parar)
            # print(self.getTextoProcesado())

        # Pagina 4
        paginaCuatro = self.stackedWidget.widget(3)
        inputMostrar = paginaCuatro.findChild(QtWidgets.QLineEdit, "inputMostrar")
        inputVistaPrevia = paginaCuatro.findChild(QtWidgets.QLineEdit, "inputVistaPrevia")
        botonAceptar = paginaCuatro.findChild(QtWidgets.QPushButton, "botonAceptar")
        botonReintentar = paginaCuatro.findChild(QtWidgets.QPushButton, "botonReintentar")

        # print(self.getTextoReconocido(), self.getTextoProcesado())
        # inputMostrar.setText(self.getTextoReconocido())
        # inputVistaPrevia.setText(self.getTextoProcesado())

        def aceptar():
            #Enviar dirección del archivo y texto reconocido al Franco para que lo inserte
            print("aceptar")
        
        def reintentar():
            self.stackedWidget.setCurrentWidget(self.page_2)
        
        if botonAceptar:
            botonAceptar.clicked.connect(aceptar)
        
        if botonReintentar:
            botonReintentar.clicked.connect(reintentar)
    
def getDireccionArchivo():
    global direccionArchivo
    return direccionArchivo

def setDireccionArchivo(texto):
    global direccionArchivo 
    direccionArchivo = texto

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
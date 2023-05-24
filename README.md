# Programacion por Voz

"Programación por Voz" es una aplicación que permite escribir código Python mediante comandos de voz. Al activar el micrófono, el programa comienza a escuchar las instrucciones del usuario. Posteriormente, traduce dinámicamente estas instrucciones en sintaxis de Python, utilizando palabras clave que se han definido en orden jerárquico.

## Detalles y características principales

Al ejecutar el programa, se solicita al usuario que proporcione las instrucciones del código deseado a través de una grabación de voz. Luego, el programa procesa las palabras mencionadas por el usuario y las compara con grupos de palabras clave definidos por los programadores. Los grupos principales de palabras clave incluyen: crear, llamar, eliminar, asignar, comentar, mover e insertar. Estos grupos contienen palabras adicionales como bucle, comentario, condicional, función, lista y variable.
Una vez que se encuentran coincidencias entre las palabras del usuario y los grupos de palabras clave, la información se envía a una aplicación encargada de traducirla a comandos en lenguaje Python. El programa crea entonces un archivo ".py" que contiene las instrucciones del usuario traducidas a código, listo para ser ejecutado.
Esta aplicación resulta sumamente útil al crear programas en Python, ya que agiliza considerablemente el proceso de escritura de código. Además, al basarse en un lenguaje cotidiano, es muy sencillo obtener el código deseado simplemente solicitándoselo al programa.

## Instrucciones de instalación

A continuación, se proporcionarán instrucciones para instalar el programa en una máquina virtual de Linux desde la consola. Estas instrucciones abarcarán los siguientes pasos: Instalación de Python, instalación de Git, instalación de pip, instalación de librerías que utiliza el proyecto, clonación del repositorio del proyecto a una carpeta local, y finalmente la ejecución de la aplicación.

### Instalación de Python desde la terminal de Linux
En ubuntu y Debian:
	-sudo apt update (Actualiza los paquetes del sistema)
	-sudo apt install python (Instala python3)
En CentOS y Fedora:
	-sudo <dnf o yum> uptate (Actualiza los paquetes del sistema)
	-sudo <dnf o yum> install python (Instala python3)

### Instalación de Git desde la terminal de Linux:
En ubuntu o Debian:
	-sudo apt install git
En CentOS y Fedora:
	-sudo <dnf o yum> install git
  
### Instalación de pip desde la terminal de Linux:
sudo apt install python-pip
  
### Instalación de librerías a utilizar
-pip install SpeechRecognition
-pip install PyAudio (previamente debemos instalar la dependencia portaudio-devel con el comando: sudo apt-get install portaudio19-dev

### Clonación del repositorio
-cd <ruta en la que se creará el repositorio local>
-git clone https://github.com/MIsabelJ/ProgramacionPorVoz.git
  
### Ejecución del programa
-cd <ruta donde se encuentra el archivo a ejecutar>
-python <archivo main a ejecutar>

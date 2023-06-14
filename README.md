# Programacion por Voz

"Programación por Voz" es una aplicación que permite escribir código Python mediante comandos de voz. Al activar el micrófono, el programa comienza a escuchar las instrucciones del usuario. Finalmente, estas instrucciones son recibidas por una extensión de una inteligencia artificial, traduciendolas a líneas de código aptas para Python. 

## Detalles y características principales

Al ejecutar el programa, se solicita al usuario que proporcione las instrucciones del código deseado a través de una grabación de voz. 
Esta grabación es almacenada y transportada a una inteligencia artificial impulsada por AutoGPT 3.5, la cual traduce nuestro mensaje en lenguaje natural a líneas de código para su uso en Python, basándose en prompts ya preestablecidas más las ingresadas por el usuario.
Así se logra otorgar una mayor libertad y margen de expresión al usuario. También la IA recibe un “archivo.py”, el cual debe ser uno ya existente, para modificarlo según lo indicado.
Esta aplicación resulta sumamente útil al crear programas en Python, ya que agiliza considerablemente el proceso de escritura de código. Además, al basarse en un lenguaje cotidiano, es muy sencillo obtener el código deseado simplemente solicitándolo al programa.


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
-pip install PyQt5
-pip install openai
-sudo apt install libxcb-xinerama0
	
En caso de tener problemas con el sonido en linux se pueden seguir estas posibles soluciones:

1-Si está en una máquina virtual como VirtualBox, active el ingreso de audio en Configuración/Sonido
2-Es probable que el problema se de también por no tener actualizados o instalados los drivers de sonido, para solucionarlo ejecute el siguiente comando en la terminal de linux: sudo apt install alsa-base alsa-utils

Una vez instalados todos los paquetes, es necesario colocar una key obtenida desde la pagina de la plataforma de Openai (https://platform.openai.com/account/api-keys) en la línea 5 del archivo prompt.py ubicado en la dirección “ProgramaciónPorVoz/textProcessing/processing”


### Clonación del repositorio
-cd "ruta en la que se creará el repositorio local"
-git clone https://github.com/MIsabelJ/ProgramacionPorVoz.git

### Ejecución del programa
-cd "ruta Interfaz gráfica"

-python -m main.py


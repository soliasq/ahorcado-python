NOMBRE: 		PORFIRIO ELIAS QUISPE QUISPE<br>
JERRY CUSUHE<br>
DAYBI SELIS MAMANI <br>
CARRERA: 	INGENIERIA DE SISTEMAS<br>
MATERIA:		SIS-111 INTRO A PROGRAMACION<br>
SEMESTRE:	 I <br>
PARALELO:	 A<br>
GESTION: 		I - 2024<br>
 Librerías<br>
En el juego de ahorcado en tkinter que hemos desarrollado, se utilizan varias funciones y bibliotecas de Python para diferentes propósitos. Aquí te explico cómo se usan y cómo instalar algunas de las bibliotecas más comunes que podrías necesitar:<br>
Funciones y Bibliotecas Utilizadas en el Juego de Ahorcado:<br>
1.	tkinter (import tkinter as tk):<br>
o	Uso: Se utiliza para construir la interfaz gráfica del juego.<br>
o	Instalación: Generalmente, tkinter ya está incluido en la instalación estándar de Python. Si necesitas verificar o instalarlo:<br>
	Linux: sudo apt-get install python3-tk<br><br>
	Windows: Viene preinstalado con las distribuciones de Python oficiales.<br>
	macOS: Ya viene incluido en las distribuciones de Python.<br>
2.	random (import random):<br>
o	Uso: Se utiliza para seleccionar aleatoriamente una palabra del conjunto de palabras disponibles.<br>
o	Instalación: Es parte de la biblioteca estándar de Python, por lo que no requiere instalación adicional.<br>
3.	tk.messagebox (from tkinter import messagebox):<br>
o	Uso: Se utiliza para mostrar mensajes emergentes con información sobre el progreso del juego, como ganar, perder o advertencias.<br>
o	Instalación: Parte de tkinter, por lo que no requiere instalación adicional.<br>
Instalación de tkinter en Linux:<br>
En distribuciones basadas en Debian, como Ubuntu, puedes instalar tkinter para Python 3 con el siguiente <br>comando:<br>
bash<br>
Copy code<br>
sudo apt-get install python3-tk<br>
Instalación de tkinter en Windows:<br>
En Windows, tkinter generalmente viene preinstalado con las distribuciones estándar de Python. Asegúrate de tener Python instalado y tkinter debería estar listo para ser utilizado.<br>
Verificación de tkinter en macOS:<br>
En macOS, tkinter también viene preinstalado con Python. Puedes verificar su disponibilidad ejecutando un script que importe tkinter desde la línea de comandos de Python.<br>
bash<br>
Copy code<br>
python3 -c "import tkinter"<br>
Conclusiones:<br>
•	tkinter es ampliamente utilizada para desarrollar aplicaciones de escritorio simples en Python debido a su facilidad de uso y su integración directa con el lenguaje.<br>
•	random es ideal para operaciones de generación aleatoria, como seleccionar palabras al azar en nuestro juego.<br>
•	tk.messagebox facilita la presentación de mensajes emergentes informativos, útiles para comunicar resultados y estados dentro del juego.<br>
Espero que esta información te haya sido útil. Si necesitas más detalles o tienes alguna otra pregunta, no dudes en preguntar.<br>
Funciones del Juego<br>
En el juego de ahorcado que desarrollamos, se utilizan varias funciones para manejar diferentes aspectos del juego. Aquí te detallo las funciones principales que se <br>implementaron y su propósito dentro del juego:<br>
1.	obtener_palabra_aleatoria():<br>
o	Propósito: Esta función elige aleatoriamente una palabra de una lista predefinida de palabras. Esta palabra es la que el jugador debe adivinar.<br>
o	Implementación: Utiliza la biblioteca random de Python para seleccionar aleatoriamente un elemento de la lista de palabras.<br>
2.	reiniciar_juego():<br>
o	Propósito: Reinicia todos los valores necesarios para comenzar un nuevo juego, incluyendo la elección de una nueva palabra aleatoria, reinicio de intentos y letras <br>adivinadas.<br>
o	Implementación: Actualiza las variables globales palabra, letras_adivinadas e intentos, además de actualizar la interfaz gráfica para reflejar el reinicio del juego.<br>
3.	actualizar_palabra_mostrada():<br>
o	Propósito: Actualiza la etiqueta en la interfaz gráfica que muestra la palabra que el jugador está adivinando, mostrando las letras adivinadas y ocultando las no adivinadas <br>con guiones bajos.<br>
o	Implementación: Itera sobre la palabra elegida (palabra) y compara cada letra con las letras adivinadas (letras_adivinadas), actualizando la etiqueta de acuerdo.<br>
4.	ingresar_letra():<br>
o	Propósito: Maneja la entrada de letras del jugador, valida si la letra ingresada es válida, comprueba si está en la palabra elegida y actualiza el juego en consecuencia.<br>
o	Implementación: Verifica la longitud y validez de la letra ingresada, muestra mensajes de error o advertencia según corresponda, actualiza los intentos restantes y verifica si el jugador ha ganado o perdido.<br>
5.	dibujar_ahorcado(intentos):<br>
o	Propósito: Dibuja las partes del ahorcado en el canvas según los intentos restantes del jugador.<br>
o	Implementación: Utiliza el canvas de tkinter para dibujar líneas y formas que representan las partes del ahorcado (poste, cuerda, cabeza, torso, brazos y piernas), con colores y dimensiones definidos.<br>
6.	ajustar_ventana():<br>
o	Propósito: Ajusta dinámicamente el tamaño de la ventana principal de acuerdo al contenido que se muestra en ella, evitando el desbordamiento y asegurando una presentación <br>adecuada.<br>
o	Implementación: Calcula el tamaño óptimo basado en el contenido actual de la ventana y la reubica en el centro de la pantalla.<br>

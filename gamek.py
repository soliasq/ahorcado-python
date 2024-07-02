import tkinter as tk
from tkinter import messagebox
import random
import pygame
import os

# Colores especificados
color_fondo = "#f0f0f0"  # Fondo más claro
color_boton = "#DDBB12"  # Azul oscuro para botones
color_texto = "#000000"  # Texto negro
color_ahorcado = "#333333"  # Color oscuro para el ahorcado

# Inicializar Pygame para manejar el audio
pygame.mixer.init()

# Función para obtener una palabra aleatoria
def obtener_palabra_aleatoria():
    palabras = ['apio', 'lechuga', 'tomate', 'zapallo', 'cebolla']
    return random.choice(palabras)

# Función para reiniciar el juego
def reiniciar_juego():
    global palabra, letras_adivinadas, intentos
    palabra = obtener_palabra_aleatoria()
    letras_adivinadas = []
    intentos = 0
    actualizar_palabra_mostrada()
    dibujar_ahorcado(intentos)
    ajustar_ventana()

# Función para actualizar la palabra mostrada en la interfaz
def actualizar_palabra_mostrada():
    estado = ' '.join([letra if letra in letras_adivinadas else '_' for letra in palabra])
    palabra_label.config(text=estado)

# Función para manejar la entrada del usuario
def ingresar_letra():
    global intentos
    letra = entrada.get().lower()
    entrada.delete(0, tk.END)

    if len(letra) != 1 or not letra.isalpha():
        mostrar_mensaje('Error', 'Por favor, ingresa una sola letra válida.')
        return

    if letra in letras_adivinadas:
        mostrar_mensaje('Advertencia', 'Ya has ingresado esa letra antes. ¡Intenta con otra!')
        return

    letras_adivinadas.append(letra)
    if letra not in palabra:
        intentos += 1
        reproducir_sonido('sonido/error.mp3')
        mostrar_mensaje('Incorrecto', f'La letra {letra} no está en la palabra. ¡Te quedan {7 - intentos} intentos!')
    else:
        reproducir_sonido('sonido/acierto.mp3')

    actualizar_palabra_mostrada()
    dibujar_ahorcado(intentos)

    if ''.join(palabra_label.cget('text').split()) == palabra:
        mostrar_mensaje('Ganaste', '¡Felicidades! ¡Has adivinado la palabra correctamente!')
        if mostrar_confirmacion('Jugar de nuevo', '¿Quieres jugar de nuevo?'):
            reiniciar_juego()
        else:
            ventana.quit()

    if intentos == 7:
        mostrar_mensaje('Perdiste', f'¡Oh no! Te has quedado sin intentos. La palabra era: {palabra}')
        if mostrar_confirmacion('Jugar de nuevo', '¿Quieres jugar de nuevo?'):
            reiniciar_juego()
        else:
            ventana.quit()

# Función para mostrar un mensaje en una ventana emergente personalizada
def mostrar_mensaje(titulo, mensaje):
    messagebox.showinfo(titulo, mensaje)

# Función para mostrar una ventana de confirmación
def mostrar_confirmacion(titulo, mensaje):
    return messagebox.askyesno(titulo, mensaje)

# Función para reproducir sonidos
def reproducir_sonido(ruta):
    sonido_path = os.path.join(os.path.dirname(__file__), ruta)
    pygame.mixer.music.load(sonido_path)
    pygame.mixer.music.play()

# Función para dibujar el ahorcado en el Canvas
def dibujar_ahorcado(intentos):
    canvas.delete("all")
    # Base y poste minimalistas
    canvas.create_line(60, 260, 240, 260, width=4, fill=color_ahorcado)  # Base más gruesa
    canvas.create_line(100, 260, 100, 40, width=4, fill=color_ahorcado)  # Poste vertical más grueso
    canvas.create_line(100, 40, 180, 40, width=4, fill=color_ahorcado)   # Poste horizontal más grueso
    canvas.create_line(180, 40, 180, 80, width=4, fill=color_ahorcado)   # Cuerda más gruesa

    # Colores del cuerpo del ahorcado
    color_cuerpo = color_fondo
    color_cabeza = color_fondo

    # Dibujar partes del cuerpo
    if intentos > 0:  # Cabeza
        canvas.create_oval(160, 80, 200, 120, width=4, outline=color_cabeza, fill=color_cabeza)
    if intentos > 1:  # Cuerpo
        canvas.create_line(180, 120, 180, 180, width=4, fill=color_cuerpo)
    if intentos > 2:  # Brazo izquierdo
        canvas.create_line(180, 140, 150, 110, width=4, fill=color_cuerpo)
    if intentos > 3:  # Brazo derecho
        canvas.create_line(180, 140, 210, 110, width=4, fill=color_cuerpo)
    if intentos > 4:  # Pierna izquierda
        canvas.create_line(180, 180, 150, 220, width=4, fill=color_cuerpo)
    if intentos > 5:  # Pierna derecha
        canvas.create_line(180, 180, 210, 220, width=4, fill=color_cuerpo)

# Función para ajustar el tamaño de la ventana según el contenido
def ajustar_ventana():
    ventana.update_idletasks()
    width = ventana.winfo_reqwidth()
    height = ventana.winfo_reqheight()
    x = (ventana.winfo_screenwidth() // 2) - (width // 2)
    y = (ventana.winfo_screenheight() // 2) - (height // 2)
    ventana.geometry(f'{width}x{height}+{x}+{y}')

# Configuración de la interfaz gráfica
ventana = tk.Tk()
ventana.title('Juego de Ahorcado')
ventana.configure(bg=color_fondo)  # Fondo blanco crema

# Crear el Canvas para dibujar el ahorcado
canvas = tk.Canvas(ventana, width=300, height=300, bg=color_fondo, highlightthickness=0)
canvas.pack(pady=20)

estado_label = tk.Label(ventana, text='Intentos restantes: 7', bg=color_fondo, fg=color_texto, font=('Arial', 14))
estado_label.pack()

palabra_label = tk.Label(ventana, text='', bg=color_fondo, fg=color_texto, font=('Arial', 28))
palabra_label.pack()

entrada = tk.Entry(ventana, font=('Arial', 14), justify='center', width=10)
entrada.pack(pady=10)

boton_frame = tk.Frame(ventana, bg=color_fondo)  # Frame para botones con fondo blanco crema
boton_frame.pack()

boton = tk.Button(boton_frame, text='Ingresar letra', command=ingresar_letra, bg=color_boton, fg=color_texto, font=('Arial', 14), padx=20, pady=10)
boton.pack(pady=5)

# Información del desarrollador
def mostrar_datos():
    mensaje = 'Nombre: \nPORFIRIO ELIAS QUISPE QUISPE\nJERRY CUSUHUE\nDAYBI SILES MAMANI\nUniversidad: UPEA\nCarrera: INGENIERIA DE SISTEMAS\SEMESTRE : 1\nParalelo: A\nGestión: I-2024'
    mostrar_mensaje('Información', mensaje)

datos_button = tk.Button(boton_frame, text='Mostrar datos', command=mostrar_datos, bg=color_boton, fg=color_texto, font=('Arial', 14), padx=20, pady=10)
datos_button.pack(pady=5)

# Ajustar el tamaño de la ventana automáticamente según contenido
ajustar_ventana()

# Iniciar el juego
reiniciar_juego()

ventana.mainloop()

import random
# from coloroma  import  init, fore, Back, Style 
# Función para obtener una palabra aleatoria
#init()


def obtener_palabra_aleatoria():
    print("las palabras son verduras!!!!!")
    palabras = ['apio', 'lechuga', 'tomate', 'zapallo', 'cebolla']
    return random.choice(palabras)

# Función para jugar al ahorcado
def jugar_ahorcado():
    # print("\033[1;m"+"\n\n\n\n¡Bienvenido al juego de  A H O R C A D O!"+"\")
    print("\n\n\n\n¡Bienvenido al juego de  A H O R C A D O!")

    palabra = obtener_palabra_aleatoria()
    letras_adivinadas = []
    intentos = 0

    while True:
        mostrar_tablero(intentos)

        estado = ''
        for letra in palabra:
            if letra in letras_adivinadas:
                estado += letra + ' '
            else:
                estado += '_ '
        print(estado)

        if estado.replace(" ", "") == palabra:
            datos()

            print('¡Felicidades! ¡Has adivinado la palabra correctamente!')
            break

        if intentos == 7:
            print('¡Oh no! Te has quedado sin intentos. La palabra era:', palabra)
            break

        letra = input('Ingresa una letra: ').lower()

        if len(letra) != 1 or not letra.isalpha():
            print('Por favor, ingresa una sola letra válida.')
            continue

        if letra in letras_adivinadas:
            print('Ya has ingresado esa letra antes. ¡Intenta con otra!')
            continue

        letras_adivinadas.append(letra)

        if letra not in palabra:
            intentos += 1
            print('La letra', letra, 'no está en la palabra. ¡Te quedan', 7 - intentos, 'intentos!')
            
            

# Función para mostrar el tablero del ahorcado
def  datos():
    print('Nombre: PORFIRIO ELIAS QUISPE QUISPE')
    print('Universidad:UPEA')
    print('Carrera:INGENIERIA DE SISTEMAS ')
    print('Paralelo: 1MA')
    print('Gestion: 2024')
    
    
def jugarDeNuevo(): #Esta funcion devuelve True si el jugador quiere volver a jugar, 
                  #en caso contrario devuelve False
    print('¿Quieres jugar de nuevo? (si o no) presione  s para SI y n para no')
    
    return input().lower().startswith('s')


def mostrar_tablero(intentos):
    figura = [
        '''
          +---+
          |   |
              |
              |
              |
              |
        ========''',
        '''
          +---+
          |   |
          O   |
              |
              |
              |
        ========''',
        '''
          +---+
          |   |
          O   |
          |   |
              |
              |
        ========''',
        '''
          +---+
          |   |
          O   |
         /|   |
              |
              |
        ========''',
        '''
          +---+
          |   |
          O   |
         /|\\  |
              |
              |
        ========''',
        '''
          +---+
          |   |
          O   |
         /|\\  |
         /    |
              |
        ========''',
        '''
          +---+
          |   |
          O   |
         /|\\  |
         / \\  |
              |
        ========'''
    ]
    print(figura[intentos])


# Iniciar el juego
jugar_ahorcado()
if jugarDeNuevo():
    intentos=0
    mostrar_tablero(intentos)
    jugar_ahorcado()
else:
    print("se acabo el juego ADIOS\n\n")
    datos()    
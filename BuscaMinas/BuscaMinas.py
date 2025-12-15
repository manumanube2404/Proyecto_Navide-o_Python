import random

# Texto inicial introductorio
print("¡Bienvenido al Buscaminas de los pesaos!")
nivel = input("\nElige el nivel (facil, medio, dificil): ").strip().lower()

# valores predeterminados
minas = 0
casillaCerrada="."
numeros="1234567890"
letras="ABCDEFGHIJ"
filas = 0
columnas = 0

# redefinimos las variables según el nivel escogido
match nivel:
    case "facil":
        print("\nDificultad fácil seleccionada.")
        minas = 3
        filas = 6
        columnas = 6

    case "medio":
        print("\nDificultad media seleccionada.")
        minas = 6
        filas = 8
        columnas = 8

    case "dificil":
        print("\nDificultad máxima seleccionada.")
        minas = 10
        filas = 10
        columnas = 10
    case _: #el guión bajo en python significa "cualquier otro valor"
        print("La dificultad '", nivel, "' no está reconocida por el programa. Seleccionando por defecto el modo fácil.")
        minas = 3
        filas = 6
        columnas = 6
print("\nPreparando tablero de", filas, "x", columnas, "con", minas, "minas...")

# Necesitamos crear dos tableros, uno donde esté toda la información y otro que sea el que ve el jugador por consola. La lógica del juego se basará en ir actualizando el tablero que ve el jugador según las acciones que realice.
tableroCompleto = []
tableroJuego = []

for f in range(filas):
    filaCompleta = [0] * columnas
    tableroCompleto.append(filaCompleta)

    filaJuego = [casillaCerrada] * columnas
    tableroJuego.append(filaJuego)

# colocación de minas

#contador de minas
minas_colocadas = 0
while minas_colocadas < minas: #filas/columnas - 1 para asegurar que está dentro de casillas
    filaRandom = random.randint(0, filas - 1)
    columnaRandom = random.randint(0, columnas - 1)

    # La mina se va a representar como una X en el tablero completo para poder distinguirlo
    if tableroCompleto[filaRandom][columnaRandom] != 'X':
        tableroCompleto[filaRandom][columnaRandom] = 'X'
        minas_colocadas += 1
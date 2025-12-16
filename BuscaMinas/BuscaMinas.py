import random

# Texto inicial introductorio
print("¡Bienvenido al Buscaminas de los pesaos!")
nivel = input("\nElige el nivel (facil, medio, dificil): ").strip().lower()

# Definición de variables
minas = 0
casillaCerrada= " . "
minaSimbolo = " X "
numeros="1234567890"
letras="ABCDEFGHIJ"
filas = 0
columnas = 0
won = False
lost = False

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
        print("La dificultad '", nivel , "' no está reconocida por el programa. Seleccionando por defecto el modo fácil.")
        minas = 3
        filas = 6
        columnas = 6
print("\nPreparando tablero de", filas , "x", columnas, "con", minas , "minas...\n")

# Necesitamos crear dos tableros, uno donde esté toda la información y otro que sea el que ve el jugador por consola. La lógica del juego se basará en ir actualizando el tablero que ve el jugador según las acciones que realice.
# el tablero completo existeprinciplamente para que sea más claro en el debugging
def inicializar_tablero(filas, columnas, casillaCerrada):
    tableroCompleto = []
    tableroJuego = []

    for f in range(filas):
        fila_completa = [" 0 "] * columnas
        tableroCompleto.append(fila_completa)

        fila_juego = [casillaCerrada] * columnas
        tableroJuego.append(fila_juego)

    return tableroCompleto, tableroJuego

# colocación de minas
def colocar_minas(tablero, filas, columnas, minas, minaSimbolo):
    #contador de minas
    minas_colocadas = 0
    while minas_colocadas < minas: #filas/columnas - 1 para asegurar que está dentro de casillas
        # coordenadas aleatorias
        filaRandom = random.randint(0, filas - 1)
        columnaRandom = random.randint(0, columnas - 1)

        # La mina se va a representar como una X en el tablero completo para poder distinguirlo
        if tablero[filaRandom][columnaRandom] != minaSimbolo:
            tablero[filaRandom][columnaRandom] = minaSimbolo
            minas_colocadas += 1

    # Retornamos el tablero modificado con las minas
    return tablero

def imprimir_matriz(tablero):
    for fila in tablero:
        print(" ".join(map(str, fila)))

def main(filas, columnas, minas, casillaCerrada, minaSimbolo):
    tableroCompleto, tableroJuego = inicializar_tablero(filas, columnas, casillaCerrada)

    tableroCompleto = colocar_minas(tableroCompleto, filas, columnas, minas, minaSimbolo)
    print("\nTABLERO QUE VERÁ EL JUGADOR\n")
    imprimir_matriz(tableroJuego)
    print("\n","-"*37, "\n")
    print("\nTABLERO COMPLETO PARA DEBUGGEAR\n")
    imprimir_matriz(tableroCompleto)

    # Aquí iría el resto de la lógica del juego aún no hecha

# Ejecución del programa
main(filas, columnas, minas, casillaCerrada, minaSimbolo)
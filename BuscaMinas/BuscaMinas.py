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
        tableroCompleto.append([" 0 "] * columnas)

        tableroJuego.append([casillaCerrada] * columnas)

    return tableroCompleto, tableroJuego

# colocación de minas
def colocar_minas(tablero, filas, columnas, minas, minaSimbolo):
    #contador de minas
    minas_colocadas = 0
    while minas_colocadas < minas: #filas/columnas - 1 para asegurar que está dentro de casillas
        # coordenadas aleatorias
        fila, columna = random.randint(0, filas - 1), random.randint(0, columnas - 1)
        # La mina se va a representar como una X en el tablero completo para poder distinguirlo
        # Si ya hay una mina en esa posición, no hacemos nada y volvemos a generar coordenadas
        if tablero[fila][columna] != minaSimbolo:
            tablero[fila][columna] = minaSimbolo
            minas_colocadas += 1
    # Retornamos el tablero modificado con las minas
    return tablero

def imprimir_matriz(tablero):
    for fila in tablero:
        print(" ".join(map(str, fila)))

def contar_minas_alrededor(tablero, f, c, filas, columnas, minaSimbolo):
    conteo = 0
    # Recorremos el cuadrado 3x3 alrededor de la casilla (f, c)
    for i in range(max(0, f - 1), min(filas, f + 2)):
        for j in range(max(0, c - 1), min(columnas, c + 2)):
            if tablero[i][j] == minaSimbolo:
                conteo += 1
    return conteo

def revelar_vacias(tableroJuego, tableroCompleto, f, c, filas, columnas, casillaCerrada, minaSimbolo):
    # Si la casilla ya está revelada o es una mina, no hacemos nada
    if tableroJuego[f][c] != casillaCerrada or tableroCompleto[f][c] == minaSimbolo:
        return

    # Si la casilla está cerrada y no es una mina, la revelamos
    tableroJuego[f][c] = " " + str(contar_minas_alrededor(tableroCompleto, f, c, filas, columnas, minaSimbolo)) + " "

    # Si no hay minas alrededor, revelamos las casillas adyacentes
    if contar_minas_alrededor(tableroCompleto, f, c, filas, columnas, minaSimbolo) == 0:
        for i in range(max(0, f - 1), min(filas, f + 2)):
            for j in range(max(0, c - 1), min(columnas, c + 2)):
                if tableroJuego[i][j] == casillaCerrada:
                    revelar_vacias(tableroJuego, tableroCompleto, i, j, filas, columnas, casillaCerrada, minaSimbolo)

    #Pregunta al usuario la casilla que quiere marcar en un rango el 0-n
def preguntar(tableroJuego, tableroCompleto, filas, columnas, minas, minaSimbolo, casillaCerrada):
    while True:
        #Si ganar devuelve true, paramos el flujo del codigo
        if ganar(tableroJuego,filas,columnas,minas,casillaCerrada):
            print("GANASTE\nHas despejado todas las casillas!")
            break
        
        # añadimos validación en los inputs para manejar errores
        try:
            fila_prueba = int(input(f"Introduce la fila de 0 a {filas-1} : "))
            columna_prueba = int(input(f"Introduce la columna de 0 a {columnas-1}: "))
        except ValueError:
            print("Error, introduce solo números íntegros")
            continue #importante para que no se detenga el programa

        # añadimos validación de rango
        if not (0 <= fila_prueba < filas and 0 <= columna_prueba < columnas):
            print(f"Error, esa posición no existe. El rango es de 0 a {filas - 1}")
            continue
        # añadimos validación para comprobar si la casilla seleccionada está ya abierta
        if tableroJuego[fila_prueba][columna_prueba] != casillaCerrada:
            print("Esa casilla ya está abierta chavalín, elige otra")
            continue

        minasCercanas = 0 #no se si es necesaria pero no la voy a borrar por si acaso
        #Si el numero no es valido pide otro intento
            # Comprueba si la casilla es " 0 " en el mapa original
        
        if tableroCompleto[fila_prueba][columna_prueba] == minaSimbolo:
            #Si en la posicion no hay un " 0 " significa que es una mina, por lo que el jugador perdio
            imprimir_matriz(tableroCompleto)
            print("PERDISTE")
            break

        else:
            #Los bucles comprueban los alrrededores de la casilla seleccionada para saber si hay minas cerca
            #Llamamos a la funcion revelar_vacias para que revele todas las casillas vacías
            revelar_vacias(tableroJuego, tableroCompleto, fila_prueba, columna_prueba, filas, columnas, casillaCerrada, minaSimbolo)
            print("\nTablero actualizado:")
            imprimir_matriz(tableroJuego)

    
    #Si los " . " son iguales al numero de minas existentes retornamos true
def ganar(tableroJuego, filas, columnas, minas, casillaCerrada):
    puntos = 0
    for i in range(filas):
        for j in range(columnas):
            if tableroJuego[i][j] == casillaCerrada:
                puntos += 1
    return puntos == minas
        
def main(filas, columnas, minas, casillaCerrada, minaSimbolo):
    tableroCompleto, tableroJuego = inicializar_tablero(filas, columnas, casillaCerrada)
    tableroCompleto = colocar_minas(tableroCompleto, filas, columnas, minas, minaSimbolo)

    print("\nTABLERO QUE VERÁ EL JUGADOR\n")
    imprimir_matriz(tableroJuego)
    print("\n","-"*37, "\n")
    print("\nTABLERO COMPLETO PARA DEBUGGEAR\n")
    imprimir_matriz(tableroCompleto)
    preguntar(tableroJuego,tableroCompleto, filas, columnas, minas, minaSimbolo, casillaCerrada)
# Ejecución del programa
main(filas, columnas, minas, casillaCerrada, minaSimbolo)
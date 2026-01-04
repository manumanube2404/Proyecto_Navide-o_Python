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

    #Pregunta al usuario la casilla que quiere marcar en un rango el 0-n
def preguntar(tableroJuego, tableroCompleto, filas,columnas):
    while True:
        #Si ganar devuelve true, paramos el flujo del codigo
        if ganar(tableroJuego,filas,columnas):
            print("GANASTE")
            break
        fila_prueba = int(input(f"Introduce la fila de 0 a {filas-1} : "))
        columna_prueba = int(input(f"Introduce la columna de 0 a {columnas-1}: "))
        minasCercanas=0
        #Si el numero no es valido pide otro intento
        if fila_prueba >= filas or columna_prueba >= columnas:
            print("Esa posicion no existe, por favor vuelva a intentarlo")
        else:
            # Comprueba si la casilla es " 0 " en el mapa original
            if tableroCompleto[fila_prueba][columna_prueba] == " 0 ":
                #Los bucles comprueban los alrrededores de la casilla seleccionada para saber si hay minas cerca
                for i in range(-1,2):
                    for j in range (-1,2):
                        #Si las filas o las columnas no existen para la ejecucucion (>n)
                        if i==1 and fila_prueba==filas-1: 
                            break
                        if j==1 and columna_prueba==columnas-1:
                            break
                        #Cuenta si en el mapa original hay alguna " X " cerca 
                        if tableroCompleto[fila_prueba+i][columna_prueba+j] == minaSimbolo:
                            #Si las filas o las columnas no existen para la ejecucucion (<n) 
                            if fila_prueba+i!=-1 and columna_prueba+j!= -1:
                                minasCercanas+=1

                tableroJuego[fila_prueba][columna_prueba]= str(f" {minasCercanas} ")
                imprimir_matriz(tableroJuego)

            else:
                #Si en la posicion no hay un " 0 " significa que es una mina, por lo que el jugador perdio
                imprimir_matriz(tableroCompleto)
                print("PERDISTE")
                break

    
    #Si los " . " son iguales al numero de minas existentes retornamos true
def ganar(tableroJuego,filas, columnas):
    puntos=0
    for i in range(filas):
        for j in range(columnas):
            if tableroJuego[i][j] == casillaCerrada:
                puntos+=1
    if puntos==minas:
        return True
        
def main(filas, columnas, minas, casillaCerrada, minaSimbolo):
    tableroCompleto, tableroJuego = inicializar_tablero(filas, columnas, casillaCerrada)

    tableroCompleto = colocar_minas(tableroCompleto, filas, columnas, minas, minaSimbolo)
    print("\nTABLERO QUE VERÁ EL JUGADOR\n")
    imprimir_matriz(tableroJuego)
    print("\n","-"*37, "\n")
    print("\nTABLERO COMPLETO PARA DEBUGGEAR\n")
    imprimir_matriz(tableroCompleto)
    preguntar(tableroJuego,tableroCompleto, filas, columnas)
# Ejecución del programa
main(filas, columnas, minas, casillaCerrada, minaSimbolo)
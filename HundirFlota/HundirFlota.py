import random

while True:
    try:
        menu = input("¡Bienvenido al Hundir la flota del grupo de los pesaos!\nElige qué quieres hacer:\n1. Iniciar Juego\n2. Reglas\n3. Salir\nElección: ")
        opcion = int(menu)
    except ValueError:
        print("Por favor, introduce un número válido.")
        continue
    else:
        if opcion not in (1,2,3):
            print("Introduce una opción válida.")
            continue
        else:
            break

#aqui empieza el switch
if opcion == 1:
    print("Iniciando el juego Hundir la flota... Aún no está hecho.")
elif opcion == 2:
    print("Reglas del juego Hundir la flota:\n1. Cada jugador tiene una flota de barcos que debe colocar estratégicamente en el tablero.\n2. Los barcos pueden ser de diferentes tamaños y formas.\n3. Los jugadores se turnan para disparar a las coordenadas del tablero del oponente.\n4. Si un disparo alcanza un barco, se marca como 'tocado'. Si no, se marca como 'agua'.\n5. El objetivo es hundir todos los barcos del oponente antes de que hundan los tuyos.\n6. ¡Buena suerte y diviértete!:")
elif opcion == 3:
    print("Saliendo del juego. ¡Hasta luego!")
    exit()

while True:
    try:
        menu = input("Elige qué modo quieres jugar:\n1. Juego contra la computadora\n2. Juego para dos jugadores\nElección: ")
        opcion = int(menu)
    except ValueError:
        print("Por favor, introduce un número válido.")
        continue
    else:
        if opcion not in (1,2):
            print("Introduce una opción válida.")
            continue
        else:
            break

#switch de modo de juego
if opcion == 1:
    print("Elige el nivel de dificultad:")
    print("1- Fácil\n2- Medio\n3- Difícil")
    nivel = input("Nivel: ")

    while(True):
        if nivel == "1":
            break #en cada opcion generar distintos parámetros como el tamaño del tablero, el número y tamaño de los barcos o el número de disparos permitidos
        elif nivel == "2":
            break
        elif nivel == "3":
            break 
        else: 
            print("Opción inválida")

elif opcion == 2:
    print("Iniciando 1 Vs 1. Buena suerte jugadores.")
    tablero_aleatorio = input("¿Quéreis tableros aleatorios? (s/n)")
    
    while(True):
        if tablero_aleatorio == "s":
            break #aqui meter un randomizador para la posicion de los barcos
        elif tablero_aleatorio == "n":
            break
        else: 
            print("Opción inválida")


def inicializar_tablero(filas, columnas):
    tablero = []
    for _ in range(filas):
        fila = [" ~ "] * columnas  # Representa agua
        tablero.append(fila)
    return tablero



# apartado realizado por javier 22/12/2025


def imprimir_tablero(tablero, ocultar_barcos=False):
    # Imprime arriba los números 1..10 
    print("    1  2  3  4  5  6  7  8  9 10")
    letras = "ABCDEFGHIJ"

    for i in range(len(tablero)):
        fila = tablero[i]
        linea = ""

        for celda in fila:
            # Si hay barco y hay que ocultarlo, mostramos agua
            if ocultar_barcos and celda == " B ":
                linea += " ~ "
            else:
                linea += celda

        print(letras[i] + " | " + linea)


def crear_estado_jugador(filas=10, columnas=10):
    # guardamos lo básico
    return {
        "propio": inicializar_tablero(filas, columnas),
        "disparos": inicializar_tablero(filas, columnas),
        "barcos": []  # cada barco será una lista de casillas [(f,c), (f,c)...]
    }


def se_puede_colocar(tablero, casillas):
    filas = len(tablero)
    columnas = len(tablero[0])

    for (f, c) in casillas:
        #Dentro del tablero
        if f < 0 or f >= filas or c < 0 or c >= columnas:
            return False

        #No solapar
        if tablero[f][c] == " B ":
            return False

        # No tocar
        for ff in range(f - 1, f + 2):
            for cc in range(c - 1, c + 2):
                if 0 <= ff < filas and 0 <= cc < columnas:
                    if tablero[ff][cc] == " B ":
                        return False

    return True


def colocar_barco(estado_jugador, tamano):
    tablero = estado_jugador["propio"]

    while True:
        orientacion = random.choice(["H", "V"])
        fila = random.randint(0, 9)
        col = random.randint(0, 9)

        # Creamos las casillas del barco
        casillas = []
        for i in range(tamano):
            if orientacion == "H":
                casillas.append((fila, col + i))
            else:
                casillas.append((fila + i, col))

        # colocamos y guardamos
        if se_puede_colocar(tablero, casillas):
            for (f, c) in casillas:
                tablero[f][c] = " B "

            estado_jugador["barcos"].append(casillas)
            break


def colocar_flota(estado_jugador):
    flota = [5, 4, 3, 3, 2]
    for tam in flota:
        colocar_barco(estado_jugador, tam)


def iniciar_1v1(tablero_aleatorio):
    j1 = crear_estado_jugador()
    j2 = crear_estado_jugador()

    if tablero_aleatorio == "s":
        colocar_flota(j1)
        colocar_flota(j2)

    print("\nJugador 1 - Tablero propio:")
    imprimir_tablero(j1["propio"], ocultar_barcos=False)

    print("\nJugador 1 - Tablero de disparos:")
    imprimir_tablero(j1["disparos"], ocultar_barcos=False)

    print("\nJugador 2 - Tablero propio:")
    imprimir_tablero(j2["propio"], ocultar_barcos=False)

    print("\nJugador 2 - Tablero de disparos:")
    imprimir_tablero(j2["disparos"], ocultar_barcos=False)
    
    # hasta aqui lo de javier del dia 22
def main():
    tablero = inicializar_tablero(10, 10)
    for fila in tablero:
        print(" ".join(fila))
if opcion == 1:
    main()
if opcion == 2:
    iniciar_1v1(tablero_aleatorio)

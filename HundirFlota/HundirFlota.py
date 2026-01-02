import random
import os
import time

while True:
    try:
        menu = input(
            "¡Bienvenido al Hundir la flota del grupo de los pesaos!\nElige qué quieres hacer:\n1. Iniciar Juego\n2. Reglas\n3. Salir\nElección: ")
        opcion = int(menu)
    except ValueError:
        print("Por favor, introduce un número válido.")
        continue
    else:
        if opcion not in (1, 2, 3):
            print("Introduce una opción válida.")
            continue
        else:
            break

# aqui empieza el switch
if opcion == 1:
    print("Iniciando el juego Hundir la flota... Aún no está hecho.")
elif opcion == 2:
    print("Reglas del juego Hundir la flota:\n1. Cada jugador tiene una flota de barcos que debe colocar estratégicamente en el tablero.\n2. Los barcos pueden ser de diferentes tamaños y formas.\n3. Los jugadores se turnan para disparar a las coordenadas del tablero del oponente.\n4. Si un disparo alcanza un barco, se marca como 'tocado'. Si no, se marca como 'agua'.\n5. El objetivo es hundir todos los barcos del oponente antes de que hundan los tuyos.\n6. ¡Buena suerte y diviértete!:")
elif opcion == 3:
    print("Saliendo del juego. ¡Hasta luego!")
    exit()

# Raúl 21/12/2025 (solo las opciones despues de iniciar partida como vs IA o vs Jugador y modos de dificultad)
while True:
    try:
        menu = input(
            "Elige qué modo quieres jugar:\n1. Juego contra la computadora\n2. Juego para dos jugadores\nElección: ")
        opcion = int(menu)
    except ValueError:
        print("Por favor, introduce un número válido.")
        continue
    else:
        if opcion not in (1, 2):
            print("Introduce una opción válida.")
            continue
        else:
            break

# switch de modo de juego
if opcion == 1:
    print("Elige el nivel de dificultad:")
    print("1- Fácil\n2- Medio\n3- Difícil")
    nivel = input("Nivel: ")

    while (True):
        if nivel == "1":
            break  # en cada opcion generar distintos parámetros como el tamaño del tablero, el número y tamaño de los barcos o el número de disparos permitidos
        elif nivel == "2":
            break
        elif nivel == "3":
            break
        else:
            print("Opción inválida")

elif opcion == 2:
    print("Iniciando 1 Vs 1. Buena suerte jugadores.")
    tablero_aleatorio = input("¿Quéreis tableros aleatorios? (s/n)")

    while (True):
        if tablero_aleatorio == "s":
            break  # aqui meter un randomizador para la posicion de los barcos
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

# aqui voy a meter funciones para más adelante implementarlas (Raúl 23/12/2025)


# atacante --> el jugador que dispara || defensor --> el jugador que recibe el disparo || fila, col --> la coordenada (fila columna) a la que se dispara
def disparar(atacante, defensor, fila, col):
    if defensor["propio"][fila][col] == " B ":
        defensor["propio"][fila][col] = " X "  # Marca el barco como tocado
        # Marca el disparo como acierto en el tablero del atacante
        atacante["disparos"][fila][col] = " X "
        print("Tocado")
    elif defensor["propio"][fila][col] == " ~ ":
        # Marca el disparo fallido en ambos tableros
        defensor["propio"][fila][col] = " O "
        atacante["disparos"][fila][col] = " O "
        print("Agua")
    else:
        print("Coordenada ya disparada")  # Para no repetir


def pedir_coordenada():  # Funcion para pedir y validar coordenadas al usuario
    while True:
        # Pedir coordenadas y poner en mayúscula por control de errores
        coord = input("Introduce coordenada (letra y número): ").upper()
        if len(coord) >= 2:  # Condicion para control de errores si solo seescribe 1 letra
            # Convertir letra a número siendo A=0 || B=1 || C=2 etc...
            fila = ord(coord[0]) - ord("A")
            # Convierte número en índice siendo 1-->0 || 5-->4 || 10-->9
            col = int(coord[1:]) - 1
            if 0 <= fila < 10 and 0 <= col < 10:
                return fila, col  # Devuelve (fila y columna)
        print("Coordenada inválida")


def ha_perdido(estado):  # Comprueba los barcos hundidos fila por fila (B es la marca de la casilla donde hay barco sin tocar/hundir)
    for fila in estado["propio"]:
        if " B " in fila:  # Comprueba la B en cada fila y duevuelve False si la hay
            return False
    return True  # Devuelve True si no existe ninguna B en ninguna fila


# apartado realizado por javier 22/12/2025

def imprimir_tablero(tablero, ocultar_barcos=False):
    # Imprime arriba los números 1..10
    print("    1  2  3  4  5  6  7  8  9 10")
    # cadena de letra que etiqueta a cada fina
    letras = "ABCDEFGHIJ"
    # bucle que recorre las filas del tablero donde i tendra los valores de 0 a 9
    for i in range(len(tablero)):
        # fila es variable que guuarda una lista de las 10 celdas en el punto en el que crear_estado_jugador
        fila = tablero[i]

        # en la variable linea se mona lo que se imprima de la fila
        linea = ""
        # lee cada elemento de la fila
        for celda in fila:
            # Si hay barco y hay que ocultarlo, mostramos agua
            if ocultar_barcos and celda == " B ":
                linea += " ~ "
            else:
                # si no se cumple se añade el contenido de esa celda a la linea
                linea += celda
        # al final se imprime la letra por la que va el programa y la linea que se forma con lo anterior
        print(letras[i] + " | " + linea)


def crear_estado_jugador(filas=10, columnas=10):
    # devuelve la estructura con datos
    return {
        # crea un tablero vacio del propio jugador
        "propio": inicializar_tablero(filas, columnas),
        # crea un tablero vacio que sirve para marcar los tiros que el jugador hace al rival
        "disparos": inicializar_tablero(filas, columnas),
        # cada barco tendra una lista de casillas [(f,c), (f,c)...]
        "barcos": []
    }

# reglas para colocar barcos


def se_puede_colocar(tablero, casillas):
    # numero de filas del talero
    filas = len(tablero)
    # numero de columnas donde tablero[0] es la primera hasta el 10
    columnas = len(tablero[0])
    # recorre cada fila
    for (f, c) in casillas:
        # se asegura de qu este dentro del tablero
        if f < 0 or f >= filas or c < 0 or c >= columnas:
            return False

        # No solapar
        if tablero[f][c] == " B ":
            return False

        # recorre las filas de alrededor
        for ff in range(f - 1, f + 2):
            # recorre columnas del alrededor
            for cc in range(c - 1, c + 2):
                # comprueba que las casillas de alrededor estan dentro del tablero
                if 0 <= ff < filas and 0 <= cc < columnas:
                    # coprueba si alrededor hay un barco para no solapar
                    if tablero[ff][cc] == " B ":
                        return False
    # si se cumple todo devuelve true
    return True

# coloca barco en el tablero con el tamaño asignado en la variable tamaño


def colocar_barco(estado_jugador, tamaño):
    # selecciona el tablero del jugador donde estan los barcos
    tablero = estado_jugador["propio"]

    while True:
        # selecciona de manera aleatoria horizontal o vertical
        orientacion = random.choice(["H", "V"])
        # selecciona de manera aleatoria una fila

        fila = random.randint(0, 9)
        # selecciona de manera aleatoria una columna

        col = random.randint(0, 9)

        # se almacena las coordenadas del barco
        casillas = []
        # recorre de i a tamaño menos 1 para construir el barco
        for i in range(tamaño):
            # si sale horizontal
            if orientacion == "H":
                # añade casilla en esa fila y sus columnas consecutivas
                casillas.append((fila, col + i))
            # si sale vertical

            else:
                # añade casilla en la fila consicutiva y en la misma columna
                casillas.append((fila + i, col))

        # se comprueba que se cumplan las caracteristicas que se definieron anteriormente
        if se_puede_colocar(tablero, casillas):

            # recorre cada casilla valida
            for (f, c) in casillas:
                # marca los barcos con B
                tablero[f][c] = " B "
            # guarda el barco en la lista de barcos del jugador
            estado_jugador["barcos"].append(casillas)
            break

# coloca todos los barcos en el tablero del jugador


def colocar_flota(estado_jugador):
    # tamaños de los barcos
    flota = [5, 4, 3, 3, 2]
    # recorre cada tamaño disponible
    for tam in flota:
        # coloca el barco del tamaño seleccionado
        colocar_barco(estado_jugador, tam)

# inicia partida 1 vs 1 donde el tablero sera o no aleatorio


def iniciar_1v1(tablero_aleatorio):
    # crea los estados de los jugadores donde estara la lista de barcos y los tableros vacios
    j1 = crear_estado_jugador()
    j2 = crear_estado_jugador()

    if tablero_aleatorio == "s":
        # en el caso de elegir aleatorio se colocaran los barcos de ambos jugadores automaticamente
        colocar_flota(j1)
        colocar_flota(j2)

    print("\nJugador 1 - Tablero propio:")
    # imprime el tablero del primer jugador mostrando los barcos
    imprimir_tablero(j1["propio"], ocultar_barcos=False)

    print("\nJugador 1 - Tablero de disparos:")
    # imprime el tablero de disparos del juagdor
    imprimir_tablero(j1["disparos"], ocultar_barcos=False)

    print("\nJugador 2 - Tablero propio:")
    # imprime el tablero del segundo jugador mostrando los barcos

    imprimir_tablero(j2["propio"], ocultar_barcos=False)

    print("\nJugador 2 - Tablero de disparos:")
    # imprime el tablero de disparos del segundo jugador
    imprimir_tablero(j2["disparos"], ocultar_barcos=False)

    print("\nJugador 2 - Tablero de disparos:")
    imprimir_tablero(j2["disparos"], ocultar_barcos=False)

    # hasta aqui lo de javier del dia 22

    # dia 29122025 trabajo javier

    while True:
        # jugador1
        print("\n tablero de disparos:")
        imprimir_tablero(j1["disparos"], ocultar_barcos=False)
        # pide las coordenadas al usuario
        fila, col = pedir_coordenada()
        # el jugador 1 dispara al jugador 2
        disparar(j1, j2, fila, col)
        # comprueba si le quedan barcos al segundo jugador para determinar el ganador
        if ha_perdido(j2):
            print("\nprimero jugador gana")
            break

        # jugador2
        print("\ntablero de disparos:")
        # muestra tablero de disparos del segundo jugador
        imprimir_tablero(j2["disparos"], ocultar_barcos=False)
        # pide coordenadas al segundo jugador
        fila, col = pedir_coordenada()
        # jugador 2 dispara al 1
        disparar(j2, j1, fila, col)
        # comprueba la cantidad de barcos del primer jugador para determinar al ganador
        if ha_perdido(j1):
            print("\nsegundo jugador gana")
            break

        # dia 29122025 trabajo javier


def main():
    tablero = inicializar_tablero(10, 10)
    for fila in tablero:
        print(" ".join(fila))


if opcion == 1:
    main()
if opcion == 2:
    iniciar_1v1(tablero_aleatorio)

    # Fran 30/12/2025 (Aquí vamos a añadir el modo contra le IA, que seria la opcion juego contra la computadora y algunas funciones extra para que el juego sea más completo)

# Funciones añadidas

# Limpia la pantalla de la consola para que otros jugadores no puedan ver tus movimientos


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def barco_hundido(estado, fila, col):

    # Comprueba si el disparo ha hundido un barco completo

    for barco in estado["barcos"]:
        if (fila, col) in barco:
            for (f, c) in barco:
                if estado["propio"][f][c] == " B ":
                    return False
            return True
    return False


# Colocación manual de barcos

def colocar_barco_manual(estado, tamano):

    # Muestra el tablero

    imprimir_tablero(estado["propio"], ocultar_barcos=False)
    print(f"Coloca un barco de tamaño {tamano}")

    while True:
        orientacion = input("Orientación (H/V): ").upper()
        if orientacion not in ("H", "V"):
            print("Orientación no válida")
            continue

            # pide la coordenada inicial
        try:
            fila, col = pedir_coordenada()
        except:
            print("Coordenada no válida")
            continue

            # genera las casillas que ocupará el barco
        casillas = []
        for i in range(tamano):
            if orientacion == "H":
                casillas.append((fila, col + i))
            else:
                casillas.append((fila + i, col))

        # Comprueba si la casilla es válida para colocar el barco y lo coloca
        if se_puede_colocar(estado["propio"], casillas):
            for (f, c) in casillas:
                estado["propio"][f][c] = " B "
            estado["barcos"].append(casillas)
            break
        else:
            print("No puedes colocar este barco ahí")


def colocar_flota_manual(estado):
    flota = [5, 4, 3, 3, 2]
    for tam in flota:
        limpiar_pantalla()
        colocar_barco_manual(estado, tam)


# Fran 31/12/2025 (Aquí implementamos el modo contra la IA con distintos niveles de dificultad)

# Funcionamiento de la IA para el 1 vs computadora

def disparo_ia_facil():
    return random.randint(0, 9), random.randint(0, 9)


def disparo_ia_medio(tablero):
    # disparo aleatorio pero evita repetir
    while True:
        f = random.randint(0, 9)
        c = random.randint(0, 9)
        if tablero[f][c] == " ~ ":
            return f, c


def disparo_ia_dificil(estado):
    # intenta buscar alrededor de tocados
    for f in range(10):
        for c in range(10):
            if estado["propio"][f][c] == " X ":
                vecinos = [(f+1, c), (f-1, c), (f, c+1), (f, c-1)]
                for vf, vc in vecinos:
                    if 0 <= vf < 10 and 0 <= vc < 10:
                        return vf, vc
    return disparo_ia_facil()


def iniciar_vs_ia(nivel):
    jugador = crear_estado_jugador()
    ia = crear_estado_jugador()

    # colocación del jugador
    elegir = input(
        "¿Quieres implementar una colocación manual? (s/n): ").lower()
    if elegir == "s":
        colocar_flota_manual(jugador)
    else:
        colocar_flota(jugador)

    # IA siempre automática
    colocar_flota(ia)

    # bucle principal de la partida

    while True:
        limpiar_pantalla()

    # muestra tableros

        print("\nTu tablero:")
        imprimir_tablero(jugador["propio"], ocultar_barcos=False)

        print("\nTus disparos:")
        imprimir_tablero(jugador["disparos"], ocultar_barcos=False)

    # turno del jugador

        print("\nEs tu turno")
        f, c = pedir_coordenada()
        disparar(jugador, ia, f, c)

        # Comprueba si has ganado contra la IA

        if ha_perdido(ia):
            print("Le ganaste a ChatGPT")
            break

        # turno de la IA

        print("\nTurno de ChatGPT")
        time.sleep(1)

        if nivel == "1":
            f, c = disparo_ia_facil()
        elif nivel == "2":
            f, c = disparo_ia_medio(jugador["propio"])
        else:
            f, c = disparo_ia_dificil(jugador)

        disparar(ia, jugador, f, c)

        if ha_perdido(jugador):
            print("ChatGPT te fulminó y te ha robado el puesto de trabajo >:D")
            break


# Activacion de funciones según el menú

# Si se eligió modo 1v1 en tu menú anterior
try:
    if opcion == 2:
        iniciar_1v1(tablero_aleatorio)
except:
    pass

# Si se eligió jugar vs IA
try:
    if opcion == 1:
        iniciar_vs_ia(nivel)
except:
    pass

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

def inicializar_tablero(filas, columnas):
    tablero = []
    for _ in range(filas):
        fila = [" ~ "] * columnas  # Representa agua
        tablero.append(fila)
    return tablero

def main():
    tablero = inicializar_tablero(10, 10)
    for fila in tablero:
        print(" ".join(fila))
if opcion == 1:
    main()
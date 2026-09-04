from random import choice

# 1. Definición de funciones-

def elegir_palabra(lista_palabras):
    # El sistema elige una palabra al azar de la lista
    return choice(lista_palabras)

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    # Muestra guiones para las letras ocultas o la letra si ya fue adivinada
    tablero = []
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero.append(letra)
        else:
            tablero.append("_")
    print("\nPalabra: " + " ".join(tablero))

def pedir_letra():
    # Pide una letra y se asegura de que el usuario ingrese un dato válido
    global letra
    letra_valida = False
    while not letra_valida:
        letra = input("Elige una letra: ").lower()
        if len(letra) == 1 and letra.isalpha():
            letra_valida = True
        else:
            print("Error: Por favor, ingresa solo una letra.")
    return letra


def verificar_victoria(palabra_secreta, letras_adivinadas):
    # Revisa si todas las letras de la palabra secreta ya fueron adivinadas
    for letra in palabra_secreta:
        if letra not in letras_adivinadas:
            return False  # Si falta al menos una, aún no gana
    return True


# --- 2. CONFIGURACIÓN INICIAL ---
opciones = ["garen", "lux", "renekton", "talon", "teemo", "amumu"]
palabra_secreta = elegir_palabra(opciones)
letras_intentadas = []
vidas = 6

# --- 3. BUCLE PRINCIPAL DEL JUEGO ---
print("\n" + "=" * 40)
print("¡Bienvenido al juego del Ahorcado!")
print("=" * 40)

# El juego continúa mientras el jugador tenga vidas
while vidas > 0:
    mostrar_tablero(palabra_secreta, letras_intentadas)
    print(f"\nVidas restantes: {vidas}")
    print(f"Letras intentadas: {', '.join(letras_intentadas)}")

    # El usuario elige una letra
    letra = pedir_letra()

    # Evitamos que pierda vidas por ingresar la misma letra dos veces
    if letra in letras_intentadas:
        print("\n¡Ya intentaste con esa letra! Prueba con otra.")
        continue

    letras_intentadas.append(letra)

    # Verificamos si acertó o falló
    if letra in palabra_secreta:
        print(f"\n¡Muy bien! La letra '{letra}' está en la palabra.")

        # Comprobamos si con esta letra adivinó la palabra completa
        if verificar_victoria(palabra_secreta, letras_intentadas):
            mostrar_tablero(palabra_secreta, letras_intentadas)
            print("\n¡FELICIDADES! Has adivinado la palabra secreta y ganado el juego.")
            break  # Rompemos el bucle porque el juego terminó
    else:
        print(f"\nLo siento, la letra '{letra}' NO está en la palabra.")
        vidas -= 1  # Le restamos una vida al jugador

# Si el bucle termina porque las vidas llegaron a cero
if vidas == 0:
    print(f"\n¡Te has quedado sin vidas! Has perdido el juego.")
    print(f"La palabra secreta era: {palabra_secreta}")
from random import randint

#1. Configuración inicial y saludo.
print("Bienvenido a el juego adivina el numero")
print("\n" + "=" * 40 +"\n")
nombre = input("¿Cual es tu nombre?: ")

#2. definición de variable.

numero = randint(1,100)
intento = 0
max_intento = 8
print(f"\nBueno {nombre}, bienvenido a adivina el numero, debes adivinar un numero entre 1 y 100. Tienes {max_intento} intentos.")

#3. El bucle principal
while intento < max_intento:
    jugada = int(input("\nIntroduce un numero: "))

#sumamos el intento número uno inmediatamente.
    intento += 1

#4. Las reglas
    if jugada < 1 or jugada > 100:
        print("\n¡Error! debes adivinar un numero entre 1 y 100")

    elif jugada < numero:
        print(f"\nEl numero secreto es mayor.")

    elif jugada > numero:
        print(f"\nEl numero secreto es menor.")

#Si el número ingresado no es menor, ni mayor ... Acertó
    else:
        print(f"\n¡Felicidades {nombre}! Adivinaste el numero {jugada}, te tomo {intento} intentos.")
        break

#5. Comprobación final al agotar intentos.
if jugada != numero:
    print(f"\nHaz perdido. El numero era {numero}.")
# 1. Solicitar el texto al usuario
texto = input("Escribe el texto a tu elección: ")
texto_minusculas = texto.lower()

# 2. Solicitar las letras (usando una lista por comprensión para simplificar)
print("\nIngresa 3 letras para analizar:")
letras = [input(f"Ingresa la letra {i+1}: ").lower() for i in range(3)]

print("\n" + "="*40 + "\n")

# 3. ¿Cuántas veces aparece cada letra?
print("1. Conteo de letras:")
# Un ciclo 'for' nos evita repetir el print y el count tres veces
for letra in letras:
    cantidad = texto_minusculas.count(letra)
    print(f"Hemos encontrado la letra '{letra}' {cantidad} veces.")

# 4. Cantidad de palabras en total
print("\n2. Cantidad de palabras:")
# .split() sin nada adentro elimina problemas si el usuario pone doble espacio
palabras = texto.split()
cantidad_palabras = len(palabras)
print(f"En total, el texto contiene {cantidad_palabras} palabras.")

# 5. Primera y última letra
print("\n3. Primera y última letra del texto:")
# Validamos rápidamente que el texto no esté vacío para evitar errores
if texto:
    primera_letra = texto[0]
    ultima_letra = texto[-1]
    print(f"La primera letra del texto es '{primera_letra}'")
    print(f"La última letra del texto es '{ultima_letra}'")
else:
    print("El texto está vacío, no hay letras para mostrar.")

# 6. Texto invertido
print("\n4. Texto invertido:")
palabras.reverse()
texto_invertido = " ".join(palabras)
print(f"El texto invertido es: '{texto_invertido}'")

# 7. Buscar la palabra 'python'
print("\n5. Buscar la palabra 'python':")
# Buscamos en 'texto_minusculas' para que detecte "Python", "PYTHON" o "python"
buscar_python = "python" in texto_minusculas

diccionario_respuestas = {
    True: "La palabra 'Python' SÍ se encuentra en tu texto.",
    False: "La palabra 'Python' NO se encuentra en tu texto."
}

print(diccionario_respuestas[buscar_python])

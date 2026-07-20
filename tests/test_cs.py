import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src" / "Criptografia"))
from cs import cifrar, descifrar, mostrar_fuerza_bruta

# Ejemplos de cifrado

llave = 3

print("=" * 60)
print("CIFRADO CÉSAR")
print(f"Llave usada en los ejemplos: k = {llave}")
print("=" * 60)

# --- Ejemplo 1 ---
texto_ejemplo_1 = "HOLA UNAL"
cifrado_1 = cifrar(texto_ejemplo_1, llave)
descifrado_1 = descifrar(cifrado_1, llave)

print("\n--- Ejemplo 1 ---")
print(f"Original : {texto_ejemplo_1}")
print(f"Cifrado  : {cifrado_1}")       # Esperado: KROD XQDO
print(f"Descifrado: {descifrado_1}")

# --- Ejemplo 2 ---
texto_ejemplo_2 = "SOLO DISCRETAS"
cifrado_2 = cifrar(texto_ejemplo_2, llave)
descifrado_2 = descifrar(cifrado_2, llave)

print("\n--- Ejemplo 2 ---")
print(f"Original : {texto_ejemplo_2}")
print(f"Cifrado  : {cifrado_2}")
print(f"Descifrado: {descifrado_2}")

# --- Ejemplo 3 ---
# Nota: Ñ no está en el alfabeto inglés; se conserva sin desplazar.
texto_ejemplo_3 = "ESPAÑA CAMPEON"
cifrado_3 = cifrar(texto_ejemplo_3, llave)
descifrado_3 = descifrar(cifrado_3, llave)

print("\n--- Ejemplo 3 ---")
print(f"Original : {texto_ejemplo_3}")
print(f"Cifrado  : {cifrado_3}")
print(f"Descifrado: {descifrado_3}")

# --- Espacio para ejemplo ---
# Cambia el texto y la llave, luego descomenta las líneas siguientes.
texto_propio = "Escribe aquí tu mensaje"
llave_propia = 5

# cifrado_propio = cifrar(texto_propio, llave_propia)
# descifrado_propio = descifrar(cifrado_propio, llave_propia)
# print("\n--- Ejemplo propio ---")
# print(f"Original : {texto_propio}")
# print(f"Cifrado  : {cifrado_propio}")
# print(f"Descifrado: {descifrado_propio}")

# --- Demostración de fuerza bruta ---
# Se toma el cifrado del Ejemplo 1 y se prueban las 26 claves.
mostrar_fuerza_bruta(cifrado_1)

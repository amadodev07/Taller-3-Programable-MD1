import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src" / "Criptografia"))
from rsa import generar_llaves, cifrar, descifrar

# Ejemplos

print("=" * 60)
print("RSA DE JUGUETE")
print("=" * 60)

# --- Ejemplo obligatorio (taller) ---
# p = 61, q = 53, e = 17, M = 65
# Esperado: n = 3233, fi(n) = 3120, d = 2753, C = 2790, M = 65
p = 61
q = 53
e = 17
mensaje = 65

llaves = generar_llaves(p, q, e)
n, fi_n, e_publico, d = llaves
cifrado = cifrar(mensaje, e_publico, n)
descifrado = descifrar(cifrado, d, n)

print("\n--- Ejemplo obligatorio ---")
print(f"p = {p}, q = {q}, e = {e}, M = {mensaje}")
print(f"n = p*q              : {n}")          # Esperado: 3233
print(f"fi(n) = (p-1)(q-1)   : {fi_n}")       # Esperado: 3120
print(f"d (inverso de e)     : {d}")          # Esperado: 2753
print(f"C = M^e (mod n)      : {cifrado}")    # Esperado: 2790
print(f"M = C^d (mod n)      : {descifrado}") # Esperado: 65

# --- Ejemplo 2 ---
p2, q2, e2, mensaje2 = 11, 17, 7, 88
llaves2 = generar_llaves(p2, q2, e2)
n2, fi2, e2_pub, d2 = llaves2
cifrado2 = cifrar(mensaje2, e2_pub, n2)
descifrado2 = descifrar(cifrado2, d2, n2)

print("\n--- Ejemplo 2 ---")
print(f"p = {p2}, q = {q2}, e = {e2}, M = {mensaje2}")
print(f"n = {n2}, fi(n) = {fi2}, d = {d2}")
print(f"Cifrado  : {cifrado2}")
print(f"Descifrado: {descifrado2}")

# --- Ejemplo 3: e invalido (gcd != 1) ---
p3, q3, e3 = 7, 13, 14  # fi(n) = 72, gcd(14, 72) = 2 != 1
print("\n--- Ejemplo 3 (e invalido) ---")
print(f"p = {p3}, q = {q3}, e = {e3}")
llaves3 = generar_llaves(p3, q3, e3)
print(f"Resultado: {llaves3}")

# --- Espacio para ejemplo propio ---
# Cambia p, q, e y el mensaje; luego descomenta las lineas siguientes.
# Recuerda: p y q deben ser primos, 1 < e < fi(n) y gcd(e, fi(n)) = 1.
# El mensaje M debe cumplir 0 <= M < n.
p_propio = 19
q_propio = 23
e_propio = 5
mensaje_propio = 100

# llaves_propias = generar_llaves(p_propio, q_propio, e_propio)
# n_propio, fi_propio, e_prop, d_propio = llaves_propias
# cifrado_propio = cifrar(mensaje_propio, e_prop, n_propio)
# descifrado_propio = descifrar(cifrado_propio, d_propio, n_propio)
# print("\n--- Ejemplo propio ---")
# print(f"p = {p_propio}, q = {q_propio}, e = {e_propio}, M = {mensaje_propio}")
# print(f"n = {n_propio}, fi(n) = {fi_propio}, d = {d_propio}")
# print(f"Cifrado  : {cifrado_propio}")
# print(f"Descifrado: {descifrado_propio}")

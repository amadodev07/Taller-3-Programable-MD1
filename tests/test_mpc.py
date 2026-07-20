import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src" / "Criptografia"))
from mpc import MODULO, promedio_seguro, repartir_nota

# Ejemplos

print("=" * 60)
print("MPC BASICO - PROMEDIO SIN REVELAR NOTAS")
print(f"Modulo M = {MODULO}")
print("=" * 60)

print("\n--- Ejemplo 1 (obligatorio) ---")
# --- Ejemplo minimo (taller) ---
# Notas [40, 35, 50, 25] -> suma 150, promedio 37.5
notas1 = [40, 35, 50, 25]
suma1, promedio1 = promedio_seguro(notas1, mostrar_servidores=True)

print(f"Cantidad de notas: {len(notas1)}")
print(f"Suma reconstruida : {suma1}")       # Esperado: 150
print(f"Promedio          : {promedio1}")   # Esperado: 37.5

# --- Ejemplo 2 ---
notas2 = [50, 50, 50]
#Decído incluir las notas en el ejemplo 2
#Nótese, que en la función promedio_seguro, está desactivado el mostrar_servidores, por lo que no se imprimen las notas en los servidores.
#Si se desea imprimir las notas en los servidores, se debe activar el mostrar_servidores, descomentando la siguiente línea:
#suma2, promedio2 = promedio_seguro(notas2, mostrar_servidores=True)
suma2, promedio2 = promedio_seguro(notas2)
print("\n--- Ejemplo 2 ---")
print(f"notas2: {notas2}")
print(f"Cantidad de notas: {len(notas2)}")
print(f"Suma reconstruida : {suma2}")
print(f"Promedio          : {promedio2}")

# --- Ejemplo 3 ---
notas3 = [10, 20, 30, 40, 45, 15]
suma3, promedio3 = promedio_seguro(notas3)

print("\n--- Ejemplo 3 ---")
print(f"Cantidad de notas: {len(notas3)}")
print(f"Suma reconstruida : {suma3}")
print(f"Promedio          : {promedio3}")

# --- Demostracion: una sola parte no revela la nota ---
print("\n--- Demostracion de reparto ---")
nota_ejemplo = 40
s1, s2, s3 = repartir_nota(nota_ejemplo)
print(f"Nota original x = {nota_ejemplo}")
print(f"Partes: s1 = {s1}, s2 = {s2}, s3 = {s3}")
print(f"Chequeo: (s1 + s2 + s3) mod M = {(s1 + s2 + s3) % MODULO}")

# --- Espacio para ejemplo propio ---
# Cambia la lista de notas (enteros entre 0 y 50) y descomenta.
notas_propias = [25, 30, 40, 45, 50]

# suma_propia, promedio_propio = promedio_seguro(notas_propias, mostrar_servidores=True)
# print("\n--- Ejemplo propio ---")
# print(f"Cantidad de notas: {len(notas_propias)}")
# print(f"Suma reconstruida : {suma_propia}")
# print(f"Promedio          : {promedio_propio}")

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src" / "grafos"))
# Importamos el grafo desde el otro archivo, ruta_corta.py
from ruta_corta import grafo_ciudad
from cierre_estacion import medir_impacto, mostrar_tabla, mostrar_clasificacion

# Ejemplos

print("=" * 60)
print("CIERRE DE UNA ESTACION")
print("=" * 60)

grafo = grafo_ciudad()

# Al menos cinco pares origen-destino
pares = [
    ("Portal", "Aeropuerto"),
    ("Museo", "Usaquen"),
    ("Portal", "Chapinero"),
    ("Museo", "Aeropuerto"),
    ("Universidad", "Aeropuerto"),
    ("Centro", "Usaquen"),
]

print(f"Pares evaluados: {len(pares)}")
for origen, destino in pares:
    print(f"  {origen} -> {destino}")

# --- Ejemplo 1: cierre que afecta la mayoria (Chapinero) ---
vertice1 = "Chapinero"
filas1 = medir_impacto(grafo, pares, vertice1)

print("\n" + "=" * 60)
print(f"--- Ejemplo 1: cierre de {vertice1} (afecta la mayoria) ---")
print("=" * 60)
mostrar_tabla(filas1)
mostrar_clasificacion(filas1)

# --- Ejemplo 2: cierre que afecta una direccion (Calle26) ---
vertice2 = "Calle26"
filas2 = medir_impacto(grafo, pares, vertice2)

print("\n" + "=" * 60)
print(f"--- Ejemplo 2: cierre de {vertice2} (afecta una direccion) ---")
print("=" * 60)
mostrar_tabla(filas2)
mostrar_clasificacion(filas2)

# --- Ejemplo 3: cierre que no afecta ninguna (Soacha) ---
vertice3 = "Soacha"
filas3 = medir_impacto(grafo, pares, vertice3)

print("\n" + "=" * 60)
print(f"--- Ejemplo 3: cierre de {vertice3} (no afecta ninguna) ---")
print("=" * 60)
mostrar_tabla(filas3)
mostrar_clasificacion(filas3)

# --- Espacio para ejemplo propio ---
# Cambia el vertice cerrado o los pares, luego descomenta.
vertice_propio = "Universidad"
pares_propios = [
    ("Portal", "Aeropuerto"),
    ("Museo", "Usaquen"),
    ("Portal", "Chapinero"),
    ("Museo", "Aeropuerto"),
    ("Universidad", "Aeropuerto"),
]

# filas_propias = medir_impacto(grafo, pares_propios, vertice_propio)
# print("\n--- Ejemplo propio ---")
# print(f"Vertice cerrado: {vertice_propio}")
# mostrar_tabla(filas_propias)
# mostrar_clasificacion(filas_propias)

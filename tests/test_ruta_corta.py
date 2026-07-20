import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src" / "grafos"))
from ruta_corta import grafo_ciudad, dijkstra

# Ejemplos

print("=" * 60)
print("RUTA MAS CORTA - DIJKSTRA")
print("=" * 60)

grafo = grafo_ciudad()
print(f"Vertices: {len(grafo)}")
print(f"Aristas (dirigidas): {sum(len(v) for v in grafo.values())}")

# --- Ejemplo 1 ---
origen1, destino1 = "Portal", "Aeropuerto"
dist1, ruta1 = dijkstra(grafo, origen1, destino1)

print("\n--- Ejemplo 1 ---")
print(f"Origen  : {origen1}")
print(f"Destino : {destino1}")
print(f"Distancia: {dist1}")
print(f"Ruta    : {' -> '.join(ruta1)}")

# --- Ejemplo 2 ---
origen2, destino2 = "Museo", "Usaquen"
dist2, ruta2 = dijkstra(grafo, origen2, destino2)

print("\n--- Ejemplo 2 ---")
print(f"Origen  : {origen2}")
print(f"Destino : {destino2}")
print(f"Distancia: {dist2}")
print(f"Ruta    : {' -> '.join(ruta2)}")

# --- Ejemplo 3 ---
origen3, destino3 = "Calle26", "Chapinero"
dist3, ruta3 = dijkstra(grafo, origen3, destino3)

print("\n--- Ejemplo 3 ---")
print(f"Origen  : {origen3}")
print(f"Destino : {destino3}")
print(f"Distancia: {dist3}")
print(f"Ruta    : {' -> '.join(ruta3)}")

# --- Espacio para ejemplo propio ---
# Cambia origen y destino, luego descomenta las lineas siguientes.
origen_propio = "Universidad"
destino_propio = "Centro"

# dist_propia, ruta_propia = dijkstra(grafo, origen_propio, destino_propio)
# print("\n--- Ejemplo propio ---")
# print(f"Origen  : {origen_propio}")
# print(f"Destino : {destino_propio}")
# print(f"Distancia: {dist_propia}")
# print(f"Ruta    : {' -> '.join(ruta_propia)}")

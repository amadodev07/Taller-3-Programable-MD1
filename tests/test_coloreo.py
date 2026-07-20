import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src" / "grafos"))
from coloreo import (
    grafo_conflictos,
    coloreo_voraz,
    es_coloreado_valido,
    cantidad_colores,
    agrupar_por_color,
    mostrar_coloreo,
)

# Ejemplos

print("=" * 60)
print("COLOREO DE GRAFOS - EXAMENES SIN CHOQUES")
print("=" * 60)

grafo = grafo_conflictos()
print(f"Cursos (vertices): {len(grafo)}")
print(f"Conflictos (aristas): {sum(len(v) for v in grafo.values()) // 2}")

# --- Ejemplo 1: orden alfabetico ---
coloreo1 = coloreo_voraz(grafo)
valido1 = es_coloreado_valido(grafo, coloreo1)

print("\n--- Ejemplo 1 (orden alfabetico) ---")
print(f"Colores usados: {cantidad_colores(coloreo1)}")
print(f"Coloreo valido: {valido1}")
for color, vertices in agrupar_por_color(coloreo1).items():
    print(f"  Franja {color}: {', '.join(vertices)}")

# --- Ejemplo 2: otro orden de vertices ---
# El voraz puede usar distinta cantidad de colores segun el orden.
orden2 = [
    "Discretas",
    "Calculo",
    "BasesDatos",
    "Economia",
    "Fisica",
    "Algebra",
    "Programacion",
    "Quimica",
    "Estadistica",
    "Biologia",
    "Redes",
]
coloreo2 = coloreo_voraz(grafo, orden=orden2)
valido2 = es_coloreado_valido(grafo, coloreo2)

print("\n--- Ejemplo 2 (otro orden) ---")
print(f"Colores usados: {cantidad_colores(coloreo2)}")
print(f"Coloreo valido: {valido2}")
for color, vertices in agrupar_por_color(coloreo2).items():
    print(f"  Franja {color}: {', '.join(vertices)}")

# --- Ejemplo 3: verificacion de conflictos ---
print("\n--- Ejemplo 3 (verificacion) ---")
conflictos = 0
for curso, vecinos in grafo.items():
    for vecino in vecinos:
        if curso < vecino and coloreo1[curso] == coloreo1[vecino]:
            conflictos += 1
            print(f"  Choque: {curso} y {vecino} en franja {coloreo1[curso]}")
if conflictos == 0:
    print("  No hay cursos adyacentes con el mismo color.")

# --- Espacio para ejemplo propio ---
# Cambia el orden (o el grafo en coloreo.py) y descomenta.
orden_propio = [
    "Redes",
    "Biologia",
    "Economia",
    "Quimica",
    "BasesDatos",
    "Estadistica",
    "Programacion",
    "Discretas",
    "Fisica",
    "Algebra",
    "Calculo",
]

# coloreo_propio = coloreo_voraz(grafo, orden=orden_propio)
# print("\n--- Ejemplo propio ---")
# mostrar_coloreo(coloreo_propio, grafo)

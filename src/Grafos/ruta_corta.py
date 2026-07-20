"""
Punto 4 - Ruta mas corta (Dijkstra)
"""

import math


def grafo_ciudad():
    """
    Grafo ponderado de prueba.
    9 vertices y mas de 12 aristas, pesos positivos.
    """
    # Estructura del grafo: cada arista es (a, b, peso)
    # a = vertice origen, b = vertice destino, peso = costo.
    # Para cargar un grafo distinto, agregue o reemplace tuplas siguiendo
    # esa misma forma: ("VerticeA", "VerticeB", peso).
    # Ejemplo: ("Portal", "Calle26", 8) significa Portal --8-- Calle26.
    aristas = [
        ("Portal", "Calle26", 8),
        ("Portal", "Universidad", 20),
        ("Calle26", "Museo", 5),
        ("Calle26", "Centro", 12),
        ("Museo", "Centro", 7),
        ("Museo", "Universidad", 10),
        ("Centro", "Chapinero", 9),
        ("Universidad", "Chapinero", 6),
        ("Universidad", "Usaquen", 15),
        ("Chapinero", "Usaquen", 8),
        ("Chapinero", "Aeropuerto", 25),
        ("Usaquen", "Aeropuerto", 18),
        ("Centro", "Aeropuerto", 30),
        # Estacion periferica: no interviene en las rutas centrales de prueba
        ("Portal", "Soacha", 5),
    ]

    grafo = {}
    for origen, destino, peso in aristas:
        if origen not in grafo:
            grafo[origen] = {}
        if destino not in grafo:
            grafo[destino] = {}
        grafo[origen][destino] = peso
        grafo[destino][origen] = peso

    return grafo


def dijkstra(grafo, origen, destino):
    """
    Encuentra la ruta de menor costo entre origen y destino.
    Devuelve (distancia_total, ruta) o (None, None) si no hay camino.
    """
    if origen not in grafo or destino not in grafo:
        return None, None

    distancias = {vertice: math.inf for vertice in grafo}
    distancias[origen] = 0
    anteriores = {vertice: None for vertice in grafo}
    pendientes = set(grafo.keys())

    while pendientes:
        # Vertice pendiente con menor distancia conocida
        actual = min(pendientes, key=lambda v: distancias[v])
        pendientes.remove(actual)

        if distancias[actual] == math.inf:
            break
        if actual == destino:
            break

        for vecino, peso in grafo[actual].items():
            if vecino not in pendientes:
                continue
            nueva_distancia = distancias[actual] + peso
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                anteriores[vecino] = actual

    if distancias[destino] == math.inf:
        return None, None

    # Reconstruye la ruta de destino hacia origen
    ruta = []
    actual = destino
    while actual is not None:
        ruta.append(actual)
        actual = anteriores[actual]
    ruta.reverse()

    return distancias[destino], ruta

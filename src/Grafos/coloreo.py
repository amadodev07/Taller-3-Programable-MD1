"""
Punto 6 - Coloreo de grafos (examenes sin choques)
"""


def grafo_conflictos():
    """
    Grafo de conflictos entre cursos (sin pesos).
    Minimo 10 vertices: cada arista indica estudiantes en comun.
    """
    # Estructura del grafo: cada arista es (a, b)
    # a y b son cursos que no pueden examinar al mismo tiempo.
    # Para cargar un grafo distinto, agregue o reemplace tuplas:
    # ("CursoA", "CursoB").
    aristas = [
        ("Calculo", "Algebra"),
        ("Calculo", "Fisica"),
        ("Calculo", "Programacion"),
        ("Algebra", "Discretas"),
        ("Algebra", "Estadistica"),
        ("Fisica", "Quimica"),
        ("Fisica", "Discretas"),
        ("Programacion", "Discretas"),
        ("Programacion", "BasesDatos"),
        ("Discretas", "Estadistica"),
        ("Discretas", "BasesDatos"),
        ("Quimica", "Biologia"),
        ("Quimica", "Estadistica"),
        ("Estadistica", "Economia"),
        ("BasesDatos", "Redes"),
        ("BasesDatos", "Economia"),
        ("Biologia", "Economia"),
        ("Biologia", "Redes"),
        ("Economia", "Redes"),
        ("Calculo", "Estadistica"),
    ]

    grafo = {}
    for a, b in aristas:
        if a not in grafo:
            grafo[a] = set()
        if b not in grafo:
            grafo[b] = set()
        grafo[a].add(b)
        grafo[b].add(a)

    return grafo


def coloreo_voraz(grafo, orden=None):
    """
    Asigna el menor color disponible a cada vertice (algoritmo voraz).
    Devuelve un diccionario {vertice: color}.
    """
    if orden is None:
        orden = sorted(grafo.keys())

    coloreo = {}
    for vertice in orden:
        # Colores ya usados por los vecinos
        colores_prohibidos = {
            coloreo[vecino]
            for vecino in grafo[vertice]
            if vecino in coloreo
        }
        color = 0
        while color in colores_prohibidos:
            color += 1
        coloreo[vertice] = color

    return coloreo


def es_coloreado_valido(grafo, coloreo):
    """Verifica que no haya dos vertices adyacentes con el mismo color."""
    for vertice, vecinos in grafo.items():
        for vecino in vecinos:
            if coloreo[vertice] == coloreo[vecino]:
                return False
    return True


def cantidad_colores(coloreo):
    """Cantidad de colores distintos usados."""
    return len(set(coloreo.values()))


def agrupar_por_color(coloreo):
    """Devuelve {color: [vertices]}."""
    grupos = {}
    for vertice, color in coloreo.items():
        if color not in grupos:
            grupos[color] = []
        grupos[color].append(vertice)
    for color in grupos:
        grupos[color].sort()
    return dict(sorted(grupos.items()))


def mostrar_coloreo(coloreo, grafo=None):
    """Imprime colores usados y vertices por franja horaria."""
    print(f"Colores usados: {cantidad_colores(coloreo)}")
    if grafo is not None:
        print(f"Coloreo valido: {es_coloreado_valido(grafo, coloreo)}")
    for color, vertices in agrupar_por_color(coloreo).items():
        print(f"  Franja {color}: {', '.join(vertices)}")

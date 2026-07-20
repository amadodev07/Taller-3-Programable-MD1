"""
Punto 5 - Cierre de una estacion
"""

from ruta_corta import dijkstra


def eliminar_vertice(grafo, vertice):
    """
    Devuelve una copia del grafo sin el vertice cerrado
    y sin las aristas que lo tocaban.
    """
    nuevo_grafo = {}
    for origen, vecinos in grafo.items():
        if origen == vertice:
            continue
        nuevo_grafo[origen] = {
            destino: peso
            for destino, peso in vecinos.items()
            if destino != vertice
        }
    return nuevo_grafo


def medir_impacto(grafo, pares, vertice_cerrado):
    """
    Compara rutas mas cortas antes y despues del cierre.
    Devuelve una lista de filas:
    (origen, destino, dist_antes, dist_despues, diferencia, estado)
    """
    grafo_despues = eliminar_vertice(grafo, vertice_cerrado)
    filas = []

    for origen, destino in pares:
        dist_antes, _ = dijkstra(grafo, origen, destino)
        dist_despues, _ = dijkstra(grafo_despues, origen, destino)

        if dist_antes is None:
            estado = "sin camino antes"
            diferencia = None
        elif dist_despues is None:
            estado = "desconectado"
            diferencia = None
        elif dist_despues > dist_antes:
            estado = "aumento"
            diferencia = dist_despues - dist_antes
        else:
            estado = "igual"
            diferencia = 0

        filas.append((origen, destino, dist_antes, dist_despues, diferencia, estado))

    return filas


def mostrar_tabla(filas):
    """Imprime la tabla de impacto del cierre."""
    encabezado = (
        f"{'origen':<14} {'destino':<14} {'antes':>8} "
        f"{'despues':>8} {'dif':>8} {'estado':<14}"
    )
    print(encabezado)
    print("-" * len(encabezado))

    for origen, destino, antes, despues, diferencia, estado in filas:
        texto_antes = "-" if antes is None else str(antes)
        texto_despues = "-" if despues is None else str(despues)
        texto_dif = "-" if diferencia is None else str(diferencia)
        print(
            f"{origen:<14} {destino:<14} {texto_antes:>8} "
            f"{texto_despues:>8} {texto_dif:>8} {estado:<14}"
        )


def mostrar_clasificacion(filas):
    """Clasifica pares: aumentaron, iguales y desconectados."""
    aumentaron = [f for f in filas if f[5] == "aumento"]
    iguales = [f for f in filas if f[5] == "igual"]
    desconectados = [f for f in filas if f[5] == "desconectado"]

    print("\nDistancias que aumentaron:")
    if aumentaron:
        for origen, destino, antes, despues, diferencia, estado in aumentaron:
            print(f"  {origen} -> {destino}: {antes} -> {despues} (+{diferencia})")
    else:
        print("  Ninguna.")

    print("\nDistancias que siguen iguales:")
    if iguales:
        for origen, destino, antes, despues, diferencia, estado in iguales:
            print(f"  {origen} -> {destino}: {antes}")
    else:
        print("  Ninguna.")

    print("\nPares desconectados:")
    if desconectados:
        for origen, destino, antes, despues, diferencia, estado in desconectados:
            print(f"  {origen} -> {destino}: antes {antes}, ahora sin camino")
    else:
        print("  Ninguno.")

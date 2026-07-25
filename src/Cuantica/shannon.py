"""
Punto 9 Entropia de Shannon
"""

import math


def frecuencias(texto):
    """Cuenta la frecuencia de cada simbolo del texto."""
    conteo = {}
    for simbolo in texto:
        if simbolo not in conteo:
            conteo[simbolo] = 0
        conteo[simbolo] += 1
    return conteo


def probabilidades(texto):
    """Calcula la probabilidad de cada simbolo."""
    conteo = frecuencias(texto)
    total = len(texto)
    if total == 0:
        return {}
    return {simbolo: veces / total for simbolo, veces in conteo.items()}


def entropia(texto):
    """
    Entropia de Shannon en bits:
    H = -sum(p * log2(p)) sobre los simbolos con p > 0.
    """
    probs = probabilidades(texto)
    h = 0.0
    for p in probs.values():
        if p > 0:
            h -= p * math.log2(p)
    return h


def analizar_texto(texto, nombre=""):
    """Imprime frecuencias, probabilidades y entropia de un texto."""
    if nombre:
        print(f"Texto ({nombre}): {texto!r}")
    else:
        print(f"Texto: {texto!r}")

    conteo = frecuencias(texto)
    probs = probabilidades(texto)
    h = entropia(texto)

    print(f"Longitud     : {len(texto)}")
    print(f"Simbolos     : {len(conteo)}")
    print("Frecuencias  :")
    for simbolo in sorted(conteo.keys()):
        print(f"  {simbolo!r}: {conteo[simbolo]}")
    print("Probabilidades:")
    for simbolo in sorted(probs.keys()):
        print(f"  {simbolo!r}: {probs[simbolo]:.4f}")
    print(f"Entropia H   : {h:.4f} bits")
    return h


def comparar_textos(texto1, texto2, nombre1="texto 1", nombre2="texto 2"):
    """
    Compara dos textos y explica cual tiene mayor entropia.
    """
    print(f"{nombre1}")
    h1 = analizar_texto(texto1, nombre1)
    print()
    print(f"{nombre2}")
    h2 = analizar_texto(texto2, nombre2)
    print()
    print("Comparacion")
    if abs(h1 - h2) < 1e-9:
        print("Ambos textos tienen la misma entropia.")
    elif h1 > h2:
        print(f"Mayor entropia: {nombre1} ({h1:.4f} > {h2:.4f})")
        print("Porque sus simbolos estan mejor repartidos (mas incertidumbre).")
    else:
        print(f"Mayor entropia: {nombre2} ({h2:.4f} > {h1:.4f})")
        print("Porque sus simbolos estan mejor repartidos (mas incertidumbre).")
    return h1, h2

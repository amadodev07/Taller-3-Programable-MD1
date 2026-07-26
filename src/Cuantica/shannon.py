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


def construir_arbol_huffman(conteo):
    """
    Construye el arbol de Huffman a partir de frecuencias.
    Cada nodo es [frecuencia, simbolo_o_None, izq, der].
    """
    if not conteo:
        return None

    nodos = [[veces, simbolo, None, None] for simbolo, veces in conteo.items()]

    # Un solo simbolo: codigo "0"
    if len(nodos) == 1:
        return nodos[0]

    while len(nodos) > 1:
        nodos.sort(key=lambda n: n[0])
        izq = nodos.pop(0)
        der = nodos.pop(0)
        padre = [izq[0] + der[0], None, izq, der]
        nodos.append(padre)

    return nodos[0]


def _asignar_codigos(nodo, prefijo, codigos):
    """Recorre el arbol y asigna bits a cada hoja."""
    if nodo is None:
        return
    # Hoja: tiene simbolo
    if nodo[1] is not None:
        codigos[nodo[1]] = prefijo if prefijo else "0"
        return
    _asignar_codigos(nodo[2], prefijo + "0", codigos)
    _asignar_codigos(nodo[3], prefijo + "1", codigos)


def codigo_huffman(texto):
    """
    Devuelve un diccionario {simbolo: codigo_binario} con Huffman.
    """
    conteo = frecuencias(texto)
    arbol = construir_arbol_huffman(conteo)
    codigos = {}
    _asignar_codigos(arbol, "", codigos)
    return codigos


def longitud_promedio_huffman(texto):
    """
    Longitud promedio del codigo: L = sum p_i * longitud(codigo_i).
    """
    probs = probabilidades(texto)
    codigos = codigo_huffman(texto)
    if not probs:
        return 0.0
    L = 0.0
    for simbolo, p in probs.items():
        L += p * len(codigos[simbolo])
    return L


def comparar_huffman_entropia(texto, nombre=""):
    """
    Compara la entropia H con la longitud promedio L del codigo Huffman.
    En teoria: H <= L < H + 1.
    """
    h = entropia(texto)
    L = longitud_promedio_huffman(texto)
    codigos = codigo_huffman(texto)

    if nombre:
        print(f"Huffman ({nombre})")
    else:
        print("Huffman")

    print("Codigos:")
    for simbolo in sorted(codigos.keys()):
        print(f"  {simbolo!r}: {codigos[simbolo]}")
    print(f"Entropia H              : {h:.4f} bits")
    print(f"Longitud promedio L     : {L:.4f} bits/simbolo")
    print(f"Diferencia L - H        : {L - h:.4f}")
    if h <= L + 1e-9:
        print("Se cumple H <= L (el codigo no puede ir por debajo de la entropia).")
    return h, L, codigos

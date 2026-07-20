"""
Punto 3 - MPC basico (promedio sin revelar notas)
"""

import random

MODULO = 1000003  # M suficientemente grande


def repartir_nota(nota, modulo=MODULO):
    """
    Parte una nota x en tres valores aleatorios s1, s2, s3
    tales que s1 + s2 + s3 ≡ x (mod M).
    Una sola parte no revela x.
    """
    s1 = random.randint(0, modulo - 1)
    s2 = random.randint(0, modulo - 1)
    s3 = (nota - s1 - s2) % modulo
    return s1, s2, s3


def distribuir_entre_servidores(notas, modulo=MODULO):
    """
    Cada nota se reparte en 3 partes.
    Cada servidor recibe una parte de cada nota.
    Devuelve (servidor1, servidor2, servidor3).
    """
    servidor1 = []
    servidor2 = []
    servidor3 = []

    for nota in notas:
        s1, s2, s3 = repartir_nota(nota, modulo)
        servidor1.append(s1)
        servidor2.append(s2)
        servidor3.append(s3)

    return servidor1, servidor2, servidor3


def suma_local(partes, modulo=MODULO):
    """Suma las partes que tiene un solo servidor (mod M)."""
    return sum(partes) % modulo


def reconstruir_suma(suma1, suma2, suma3, modulo=MODULO):
    """Reconstruye la suma total de las notas a partir de las 3 sumas locales."""
    return (suma1 + suma2 + suma3) % modulo


def calcular_promedio(suma_total, cantidad):
    """Promedio = suma / cantidad de notas."""
    return suma_total / cantidad


def promedio_seguro(notas, modulo=MODULO, mostrar_servidores=False):
    """
    Protocolo completo: reparte, suma por servidor y reconstruye
    solo la suma y el promedio (no las notas individuales).
    """
    if len(notas) == 0:
        raise ValueError("La lista de notas no puede estar vacia.")

    servidor1, servidor2, servidor3 = distribuir_entre_servidores(notas, modulo)

    if mostrar_servidores:
        print(f"  Servidor 1 ve: {servidor1}")
        print(f"  Servidor 2 ve: {servidor2}")
        print(f"  Servidor 3 ve: {servidor3}")

    suma1 = suma_local(servidor1, modulo)
    suma2 = suma_local(servidor2, modulo)
    suma3 = suma_local(servidor3, modulo)

    suma_total = reconstruir_suma(suma1, suma2, suma3, modulo)
    promedio = calcular_promedio(suma_total, len(notas))

    return suma_total, promedio

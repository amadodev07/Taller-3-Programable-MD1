"""
Punto 10 - Simulador basico de un qubit
"""

import math
import random

# Estado |0> = [1, 0], |1> = [0, 1]
# Compuertas como matrices 2x2

X = [
    [0, 1],
    [1, 0],
]

Z = [
    [1, 0],
    [0, -1],
]

INV_SQRT2 = 1 / math.sqrt(2)
H = [
    [INV_SQRT2, INV_SQRT2],
    [INV_SQRT2, -INV_SQRT2],
]


def estado_cero():
    """Estado inicial |0>."""
    return [1.0, 0.0]


def estado_uno():
    """Estado |1>."""
    return [0.0, 1.0]


def aplicar_compuerta(estado, matriz):
    """Aplica una compuerta (matriz 2x2) al estado del qubit."""
    a, b = estado
    nuevo_a = matriz[0][0] * a + matriz[0][1] * b
    nuevo_b = matriz[1][0] * a + matriz[1][1] * b
    return [nuevo_a, nuevo_b]


def aplicar_x(estado):
    """Compuerta X (NOT cuantico)."""
    return aplicar_compuerta(estado, X)


def aplicar_z(estado):
    """Compuerta Z."""
    return aplicar_compuerta(estado, Z)


def aplicar_h(estado):
    """Compuerta Hadamard."""
    return aplicar_compuerta(estado, H)


def probabilidades(estado):
    """
    Probabilidades de medir 0 y 1:
    P(0) = |alpha|^2, P(1) = |beta|^2.
    """
    p0 = abs(estado[0]) ** 2
    p1 = abs(estado[1]) ** 2
    return p0, p1


def medir_una_vez(estado):
    """Simula una medicion: devuelve 0 o 1 segun las probabilidades."""
    p0, _ = probabilidades(estado)
    if random.random() < p0:
        return 0
    return 1


def simular_mediciones(estado, n=1000):
    """
    Simula n mediciones independientes del mismo estado.
    Devuelve (frecuencia_0, frecuencia_1, conteo_0, conteo_1).
    """
    conteo_0 = 0
    conteo_1 = 0
    for _ in range(n):
        if medir_una_vez(estado) == 0:
            conteo_0 += 1
        else:
            conteo_1 += 1
    return conteo_0 / n, conteo_1 / n, conteo_0, conteo_1


def estados_cercanos(estado1, estado2, tolerancia=1e-9):
    """True si dos estados son iguales salvo error numerico pequeno."""
    return (
        abs(estado1[0] - estado2[0]) < tolerancia
        and abs(estado1[1] - estado2[1]) < tolerancia
    )


def mostrar_estado(estado, nombre=""):
    """Imprime el estado y sus probabilidades teoricas."""
    if nombre:
        print(f"Estado {nombre}: [{estado[0]:.6f}, {estado[1]:.6f}]")
    else:
        print(f"Estado: [{estado[0]:.6f}, {estado[1]:.6f}]")
    p0, p1 = probabilidades(estado)
    print(f"P(0) = {p0:.4f}, P(1) = {p1:.4f}")

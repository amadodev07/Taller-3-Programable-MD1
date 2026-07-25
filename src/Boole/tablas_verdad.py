"""
Punto 7 Tablas de verdad y circuitos logicos
"""

from itertools import product


def AND(x, y):
    """Conjuncion: x AND y."""
    return int(x and y)


def OR(x, y):
    """Disyuncion: x OR y."""
    return int(x or y)


def NOT(x):
    """Negacion: NOT x."""
    return int(not x)


def XOR(x, y):
    """O exclusiva: x XOR y."""
    return int(bool(x) != bool(y))


# Expresiones obligatorias del taller (variables A, B, C, D)
# 1) (A AND B) OR (NOT C)
# 2) (A XOR B) AND C
# 3) (A OR B) AND ((NOT A) OR C)

def expresion_1(A, B, C, D=0):
    """(A AND B) OR (NOT C)"""
    return OR(AND(A, B), NOT(C))


def expresion_2(A, B, C, D=0):
    """(A XOR B) AND C"""
    return AND(XOR(A, B), C)


def expresion_3(A, B, C, D=0):
    """(A OR B) AND ((NOT A) OR C)"""
    return AND(OR(A, B), OR(NOT(A), C))


def generar_combinaciones(num_variables):
    """
    Genera todas las combinaciones de 0/1 para n variables
    usando itertools.product.
    """
    return list(product([0, 1], repeat=num_variables))


def evaluar(expresion, valores, variables=("A", "B", "C", "D")):
    """
    Evalua la expresion en una entrada concreta.
    valores: dict {"A": 0/1, ...} o tupla en el orden de variables.
    """
    if isinstance(valores, dict):
        args = [valores.get(nombre, 0) for nombre in variables]
    else:
        args = list(valores)
        while len(args) < len(variables):
            args.append(0)
    return expresion(*args[:4])


def tabla_verdad(expresion, variables=("A", "B", "C", "D")):
    """
    Genera la tabla de verdad.
    Devuelve lista de (combinacion, resultado).
    """
    n = len(variables)
    filas = []
    for combinacion in generar_combinaciones(n):
        resultado = evaluar(expresion, combinacion, variables)
        filas.append((combinacion, resultado))
    return filas


def mostrar_tabla(expresion, variables=("A", "B", "C", "D"), nombre=""):
    """Imprime la tabla de verdad de forma clara."""
    if nombre:
        print(f"Expresion: {nombre}")
    encabezado = "  ".join(f"{v:>3}" for v in variables) + "  |  out"
    print(encabezado)
    print("-" * len(encabezado))
    for combinacion, resultado in tabla_verdad(expresion, variables):
        fila = "  ".join(f"{bit:>3}" for bit in combinacion)
        print(f"{fila}  |  {resultado}")

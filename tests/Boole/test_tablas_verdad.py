import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src" / "boole"))
from tablas_verdad import (
    expresion_1,
    expresion_2,
    expresion_3,
    evaluar,
    mostrar_tabla,
    AND,
    OR,
    NOT,
    XOR,
)

# Ejemplos

print("=" * 60)
print("TABLAS DE VERDAD Y CIRCUITOS LOGICOS")
print("=" * 60)

variables = ("A", "B", "C", "D")

# Ejemplo 1: (A AND B) OR (NOT C)
print("\n Ejemplo 1 ")
mostrar_tabla(expresion_1, variables, "(A AND B) OR (NOT C)")
print("Evaluacion concreta A=1, B=1, C=0, D=0:", evaluar(expresion_1, {"A": 1, "B": 1, "C": 0, "D": 0}))

# Ejemplo 2: (A XOR B) AND C
print("\n Ejemplo 2 ")
mostrar_tabla(expresion_2, variables, "(A XOR B) AND C")
print("Evaluacion concreta A=1, B=0, C=1, D=0:", evaluar(expresion_2, {"A": 1, "B": 0, "C": 1, "D": 0}))

# Ejemplo 3: (A OR B) AND ((NOT A) OR C)
print("\n Ejemplo 3 ")
mostrar_tabla(expresion_3, variables, "(A OR B) AND ((NOT A) OR C)")
print("Evaluacion concreta A=0, B=1, C=1, D=1:", evaluar(expresion_3, {"A": 0, "B": 1, "C": 1, "D": 1}))

# Espacio para ejemplo propio
# Defina su expresion (usando AND, OR, NOT, XOR).
"""
def expresion_propia(A, B, C, D):
    return AND(OR(A, B), XOR(C, D))

print("\n Ejemplo propio ")
mostrar_tabla(expresion_propia, ("A", "B", "C", "D"), "expresion propia")
print("Evaluacion:", evaluar(expresion_propia, {"A": 1, "B": 0, "C": 1, "D": 0}, ("A", "B", "C", "D")))
"""
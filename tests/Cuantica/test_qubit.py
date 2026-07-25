import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src" / "cuantica"))
from qubit import (
    estado_cero,
    aplicar_x,
    aplicar_z,
    aplicar_h,
    probabilidades,
    simular_mediciones,
    estados_cercanos,
    mostrar_estado,
)

# Ejemplos

print("=" * 60)
print("SIMULADOR BASICO DE UN QUBIT")
print("=" * 60)

#  Ejemplo 1: X|0> = |1> 
print("\n Ejemplo 1 (X|0> = |1>)")
estado = estado_cero()
mostrar_estado(estado, "|0>")
estado_x = aplicar_x(estado)
mostrar_estado(estado_x, "X|0>")
p0, p1 = probabilidades(estado_x)
print(f"Esperado: P(0)=0, P(1)=1 -> obtenido P(0)={p0:.4f}, P(1)={p1:.4f}")

# Ejemplo 2: H|0> 50% / 50%
print("\nEjemplo 2 (H|0> ~ 50/50) ")
estado_h = aplicar_h(estado_cero())
mostrar_estado(estado_h, "H|0>")
freq0, freq1, c0, c1 = simular_mediciones(estado_h, n=1000)
print(f"Mediciones (n=1000): 0 -> {c0} ({freq0:.3f}), 1 -> {c1} ({freq1:.3f})")
print("Se esperan frecuencias cercanas a 0.50 y 0.50.")

# Ejemplo 3: HH = identidad (salvo error numerico)
print("\n Ejemplo 3 (HH|0> ~= |0>)")
estado_hh = aplicar_h(aplicar_h(estado_cero()))
mostrar_estado(estado_hh, "HH|0>")
igual = estados_cercanos(estado_hh, estado_cero())
print(f"HH|0> = |0|: {igual}")

# Extra: Z sobre |0> no cambia el estado
print("\n Extra: Z|0>")
estado_z = aplicar_z(estado_cero())
mostrar_estado(estado_z, "Z|0>")

#Espacio para ejemplo propio 
# Cambia la secuencia de compuertas y descomenta.
# estado_propio = estado_cero()
# estado_propio = aplicar_h(estado_propio)
# estado_propio = aplicar_x(estado_propio)
# print("\n Ejemplo propio")
# mostrar_estado(estado_propio, "propio")
# f0, f1, n0, n1 = simular_mediciones(estado_propio, n=1000)
# print(f"Mediciones: 0 -> {n0} ({f0:.3f}), 1 -> {n1} ({f1:.3f})")

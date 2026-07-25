import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src" / "boole"))
from simplificacion import mostrar_comparacion

# Ejemplos

print("=" * 60)
print("SIMPLIFICACION BOOLEANA - QUINE-MCCLUSKEY")
print("=" * 60)

# Ejemplo 1 (taller): minterminos {1, 3, 5, 7}
print("\n Ejemplo 1 (taller: [1, 3, 5, 7])")
mostrar_comparacion([1, 3, 5, 7], ("A", "B", "C"))

# Ejemplo 2
print("\nEjemplo 2 ([0, 2, 4, 6])")
mostrar_comparacion([0, 2, 4, 6], ("A", "B", "C"))

# Ejemplo 3: 4 variables
print("\nEjemplo 3 (4 variables: [0, 1, 8, 9])")
mostrar_comparacion([0, 1, 8, 9], ("A", "B", "C", "D"))

# Espacio para ejemplo propio
# Cambia la lista de minterminos y las variables, luego descomenta.
print("\n Ejemplo propio")
mostrar_comparacion([1, 2, 3, 5], ("A", "B", "C"))

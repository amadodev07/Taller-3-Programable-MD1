import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src" / "cuantica"))
from shannon import analizar_texto, comparar_textos, entropia

# Ejemplos

print("=" * 60)
print("Entropia de Shanon")
print("=" * 60)

# Ejemplo 1: texto muy repetitivo 
texto_repetitivo = "aaaaaaaaaa"
print("\n Ejemplo 1 (repetitivo) ")
analizar_texto(texto_repetitivo, "repetitivo")

# Ejemplo 2: texto mas variado
texto_variado = "matematicas discretas"
print("\n Ejemplo 2 (variado) ")
analizar_texto(texto_variado, "variado")

# Ejemplo 3: comparacion entre ambos
print("\n Ejemplo 3 (comparacion)")
comparar_textos(texto_repetitivo, texto_variado, "repetitivo", "variado")

# Espacio para ejemplo propio
# Cambia los textos y descomenta.
# texto_propio_1 = "hola hola hola"
# texto_propio_2 = "abcdefghij"
# print("\n Ejemplo propio ")
# comparar_textos(texto_propio_1, texto_propio_2, "propio 1", "propio 2")
# print("Entropias:", entropia(texto_propio_1), entropia(texto_propio_2))

"""
Punto 2 RSA
"""


def mcd(a, b):
    """Máximo común divisor (algoritmo de Euclides)."""
    while b != 0:
        a, b = b, a % b
    return a


def euclides_extendido(a, b):
    """
    Devuelve (mcd, x, y) tales que a*x + b*y = mcd(a, b).
    Se usa para hallar el inverso modular.
    """
    if b == 0:
        return a, 1, 0
    valor_mcd, x1, y1 = euclides_extendido(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return valor_mcd, x, y


def inverso_modular(e, fi_n):
    """
    Calcula d tal que (e * d) == 1 (mod fi_n).
    Avisa y devuelve None si e no es valido (gcd(e, fi_n) != 1).
    """
    valor_mcd, x, _ = euclides_extendido(e, fi_n)
    if valor_mcd != 1:
        print(f"Advertencia: e = {e} no es valido.")
        print(f"  gcd(e, fi(n)) = {valor_mcd} != 1. No existe inverso modular.")
        return None
    # Asegura que d quede en [0, fi_n)
    d = x % fi_n
    return d


def generar_llaves(p, q, e):
    """
    A partir de primos p, q y exponente publico e calcula:
    n = p*q, fi(n) = (p-1)(q-1) y d = inverso de e mod fi(n).
    Devuelve (n, fi_n, e, d) o None si e no es valido.
    """
    n = p * q
    fi_n = (p - 1) * (q - 1)
    d = inverso_modular(e, fi_n)
    if d is None:
        return None
    return n, fi_n, e, d


def cifrar(mensaje, e, n):
    """Cifrado: C = M^e (mod n)."""
    return pow(mensaje, e, n)


def descifrar(cifrado, d, n):
    """Descifrado: M = C^d (mod n)."""
    return pow(cifrado, d, n)

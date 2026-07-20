"""
Punto 1 - Cifrado César
"""

ALFABETO_MAYUSCULAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALFABETO_MINUSCULAS = "abcdefghijklmnopqrstuvwxyz"
TAMANO_ALFABETO = 26


def cifrar(texto, llave):
    """Desplaza cada letra k posiciones hacia adelante (módulo 26)."""
    resultado = ""
    llave = llave % TAMANO_ALFABETO

    for caracter in texto:
        if caracter in ALFABETO_MAYUSCULAS:
            posicion = ALFABETO_MAYUSCULAS.index(caracter)
            nueva_posicion = (posicion + llave) % TAMANO_ALFABETO
            resultado += ALFABETO_MAYUSCULAS[nueva_posicion]
        elif caracter in ALFABETO_MINUSCULAS:
            posicion = ALFABETO_MINUSCULAS.index(caracter)
            nueva_posicion = (posicion + llave) % TAMANO_ALFABETO
            resultado += ALFABETO_MINUSCULAS[nueva_posicion]
        else:
            # Espacios, números, puntuación y ñ/Ñ se dejan igual
            resultado += caracter

    return resultado


def descifrar(texto, llave):
    """Desplaza cada letra k posiciones hacia atrás (módulo 26)."""
    return cifrar(texto, -llave)


def fuerza_bruta(texto_cifrado):
    """
    Prueba todas las claves posibles (0 a 25) cuando no se conoce k.
    Devuelve un diccionario {llave: texto_descifrado}.
    """
    intentos = {}
    for llave in range(TAMANO_ALFABETO):
        intentos[llave] = descifrar(texto_cifrado, llave)
    return intentos


def mostrar_fuerza_bruta(texto_cifrado):
    """Imprime todos los posibles descifrados."""
    print(f"Fuerza bruta sobre: '{texto_cifrado}'")
    for llave, texto in fuerza_bruta(texto_cifrado).items():
        print(f"  k = {llave:2d}  ->  {texto}")

"""
Punto 8 Simplificacion booleana
"""


def a_binario(mintermino, num_variables):
    """
    Convierte un mintermino a tupla de bits (MSB = primera variable).
    Usa division y modulo en un ciclo.
    """
    bits = []
    valor = mintermino
    for _ in range(num_variables):
        bits.append(valor % 2)
        valor = valor // 2
    bits.reverse()
    return tuple(bits)


def cuentan_unos(termino):
    """Cuenta bits en 1 (ignora guiones de no importa)."""
    return sum(1 for bit in termino if bit == 1)


def combinan(t1, t2):
    """
    Dos terminos se combinan si difieren en exactamente un bit.
    Devuelve el termino combinado con '-' en esa posicion, o None.
    """
    diferencias = 0
    combinado = []
    for a, b in zip(t1, t2):
        if a != b:
            diferencias += 1
            combinado.append("-")
        else:
            combinado.append(a)
    if diferencias == 1:
        return tuple(combinado)
    return None


def cubrir(termino, mintermino, num_variables):
    """True si el termino (con posibles '-') cubre el mintermino."""
    bits = a_binario(mintermino, num_variables)
    for t, b in zip(termino, bits):
        if t != "-" and t != b:
            return False
    return True


def termino_a_texto(termino, variables):
    """
    Convierte un termino a literal suma de productos.
    Ejemplo: (1, '-', 0) con A,B,C -> A C'
    """
    literales = []
    for bit, nombre in zip(termino, variables):
        if bit == 1:
            literales.append(nombre)
        elif bit == 0:
            literales.append(nombre + "'")
    #Caso Tautología:
    if not literales:
        return "1"
    return "".join(literales)


def quine_mccluskey(minterminos, variables=("A", "B", "C")):
    """
    Simplifica una funcion dada por minterminos.
    Devuelve (expresion_texto, lista_de_terminos_primos).
    """
    num_variables = len(variables)
    minterminos = sorted(set(minterminos))

    # Etapa 1: generar implicantes primos por agrupacion
    # Cada entrada: (termino_bits, frozenset de minterminos cubiertos)
    actuales = {}
    for m in minterminos:
        termino = a_binario(m, num_variables)
        actuales[termino] = frozenset([m])

    implicantes_primos = {}
    while actuales:
        siguientes = {}
        usados = set()
        lista = list(actuales.items())
        for i in range(len(lista)):
            for j in range(i + 1, len(lista)):
                t1, cub1 = lista[i]
                t2, cub2 = lista[j]
                comb = combinan(t1, t2)
                if comb is not None:
                    usados.add(t1)
                    usados.add(t2)
                    cobertura = cub1 | cub2
                    if comb not in siguientes or len(cobertura) > len(siguientes[comb]):
                        siguientes[comb] = cobertura
        # Los no combinados son implicantes primos
        for termino, cobertura in actuales.items():
            if termino not in usados:
                implicantes_primos[termino] = cobertura
        actuales = siguientes

    # Etapa 2: seleccionar implicantes esenciales (cubrimiento)
    faltantes = set(minterminos)
    elegidos = []

    while faltantes:
        # Esencial: unico implicante que cubre algun mintermino restante
        esencial = None
        for m in list(faltantes):
            candidatos = [
                t for t, cub in implicantes_primos.items()
                if m in cub and t not in elegidos
            ]
            if len(candidatos) == 1:
                esencial = candidatos[0]
                break

        if esencial is None:
            # Si no hay esencial, toma el que cubre mas faltantes
            mejor = None
            mejor_cuenta = -1
            for termino, cobertura in implicantes_primos.items():
                if termino in elegidos:
                    continue
                cuenta = len(cobertura & faltantes)
                if cuenta > mejor_cuenta:
                    mejor_cuenta = cuenta
                    mejor = termino
            esencial = mejor

        if esencial is None:
            break

        elegidos.append(esencial)
        faltantes -= implicantes_primos[esencial]

    textos = [termino_a_texto(t, variables) for t in elegidos]
    expresion = " + ".join(textos) if textos else "0"
    return expresion, elegidos


def evaluar_minterminos(minterminos, valores, num_variables):
    """Evalua la funcion original: 1 si el indice esta en minterminos."""
    indice = 0
    for bit in valores:
        indice = indice * 2 + bit
    return 1 if indice in minterminos else 0


def evaluar_terminos(terminos, valores):
    """Evalua la SOP simplificada (lista de terminos con 0/1/-)."""
    if not terminos:
        return 0
    for termino in terminos:
        cumple = True
        for t, v in zip(termino, valores):
            if t != "-" and t != v:
                cumple = False
                break
        if cumple:
            return 1
    return 0


def mismas_tablas(minterminos, terminos, num_variables):
    """Comprueba que original y simplificada tienen la misma tabla."""
    total = 2 ** num_variables
    for i in range(total):
        valores = a_binario(i, num_variables)
        original = evaluar_minterminos(minterminos, valores, num_variables)
        simple = evaluar_terminos(terminos, valores)
        if original != simple:
            return False
    return True


def mostrar_comparacion(minterminos, variables=("A", "B", "C")):
    """Imprime expresion simplificada y verifica equivalencia."""
    expresion, terminos = quine_mccluskey(minterminos, variables)
    equivalentes = mismas_tablas(minterminos, terminos, len(variables))
    print(f"Variables   : {', '.join(variables)}")
    print(f"Minterminos  : {sorted(set(minterminos))}")
    print(f"Simplificada: {expresion}")
    print(f"Tablas iguales: {equivalentes}")
    return expresion, terminos, equivalentes

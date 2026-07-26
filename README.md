# Taller 3 - Programacion discreta

Universidad Nacional de Colombia  
Matematicas Discretas I  
Docente: Jhoan Sebastian Tenjo Garcia

## Integrantes

- Brayan Santiago Amado Mejia bamado@unal.edu.co

## Descripción

Implementacion de los 10 puntos del taller 3, programación discreta: criptografia, grafos, algebra de Boole, Shannon y un simulador basico de qubit. Todo esta en Python, sin librerias externas.

## Lenguaje y requisitos

- Python 3.10+
- No hay que instalar nada con pip. Ver requirements.txt.
- Librerias estandar usadas: math, random, itertools, pathlib, sys.

## Estructura

```
src/
  Criptografia/   cs.py, rsa.py, mpc.py
  Grafos/         ruta_corta.py, cierre_estacion.py, coloreo.py
  Boole/          tablas_verdad.py, simplificacion.py
  Cuantica/       shannon.py, qubit.py
tests/
  Criptograf/     test_cs.py, test_rsa.py, test_mpc.py
  Grafos/         test_ruta_corta.py, test_cierre_estacion.py, test_coloreo.py
  Boole/          test_tablas_verdad.py, test_simplificacion.py
  Cuantica/       test_shannon.py, test_qubit.py
docs/
  explicacion.md  documento de explicacion del taller
requirements.txt
```

## Como ejecutar

Abrir una terminal en la carpeta raiz del proyecto (donde esta este README).

Un test puntual:

```powershell
python tests/Criptograf/test_cs.py
python tests/Criptograf/test_rsa.py
python tests/Criptograf/test_mpc.py
python tests/Grafos/test_ruta_corta.py
python tests/Grafos/test_cierre_estacion.py
python tests/Grafos/test_coloreo.py
python tests/Boole/test_tablas_verdad.py
python tests/Boole/test_simplificacion.py
python tests/Cuantica/test_shannon.py
python tests/Cuantica/test_qubit.py
```

Todos los tests de una vez (PowerShell):

```powershell
Get-ChildItem -Path tests -Recurse -Filter "test_*.py" | ForEach-Object {
  Write-Host "`n===== $($_.Name) =====" -ForegroundColor Cyan
  python $_.FullName
}
```

Si python no funciona, probar con py.

## Como hacer un ejemplo propio

En todos los archivos de tests/ hay un bloque comentado al final, tipo "ejemplo propio". Pasos:

1. Abrir el test correspondiente.
2. Cambiar las variables del ejemplo (texto, llave, notas, vertices, etc.).
3. Descomentar las lineas del bloque.
4. Volver a ejecutar ese archivo con python ....

| Punto | Archivo de test | Que cambiar |
| --- | --- | --- |
| Cesar | `tests/Criptograf/test_cs.py` | `texto_propio`, `llave_propia` |
| RSA | `tests/Criptograf/test_rsa.py` | `p_propio`, `q_propio`, `e_propio`, `mensaje_propio` |
| MPC | `tests/Criptograf/test_mpc.py` | `notas_propias` |
| Dijkstra | `tests/Grafos/test_ruta_corta.py` | `origen_propio`, `destino_propio` |
| Cierre | `tests/Grafos/test_cierre_estacion.py` | `vertice_propio`, `pares_propios` |
| Coloreo | `tests/Grafos/test_coloreo.py` | `orden_propio` |
| Tablas | `tests/Boole/test_tablas_verdad.py` | funcion `expresion_propia` |
| Simplificacion | `tests/Boole/test_simplificacion.py` | lista de minterminos |
| Shannon | `tests/Cuantica/test_shannon.py` | textos a comparar |
| Qubit | `tests/Cuantica/test_qubit.py` | secuencia de compuertas |

Para cambiar el grafo de la ciudad, editar la lista de aristas (a, b, peso) en src/Grafos/ruta_corta.py.  
Para el grafo de conflictos de examenes, editar las aristas (curso_a, curso_b) en src/Grafos/coloreo.py.

## Lista de ejercicios

1. Cifrado Cesar (`cs.py`)
2. RSA de juguete (`rsa.py`)
3. MPC basico / promedio secreto (`mpc.py`)
4. Ruta mas corta con Dijkstra (`ruta_corta.py`)
5. Cierre de una estacion (`cierre_estacion.py`)
6. Coloreo voraz de grafos (`coloreo.py`)
7. Tablas de verdad (`tablas_verdad.py`)
8. Simplificacion booleana / Quine-McCluskey (`simplificacion.py`)
9. Entropia de Shannon + Huffman (`shannon.py`)
10. Simulador de un qubit (`qubit.py`)

La explicacion matematica de cada punto esta en `docs/explicacion.md`.

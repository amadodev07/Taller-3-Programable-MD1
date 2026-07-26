# Taller 3 — Programacion discreta

**Universidad Nacional de Colombia**  
**Matematicas Discretas I**  
**Docente:** Jhoan Sebastian Tenjo Garcia
**Integrante:** Brayan Santiago Amado Mejia bamado@unal.edu.co  
**Lenguaje:** Python 3


Documento de explicacion de los 10 puntos.


## 1. Cifrado Cesar

### Que problema resuelve
Cifrar y descifrar textos con un desplazamiento fijo k, y probar todas las claves cuando k no se conoce.
### Idea matematica
Cada letra se trata como un entero en Z_26. Si x es su posicion, el cifrado es c ≡ x + k (mod 26).

### Para la documentacion
El descifrado usa el desplazamiento contrario -k porque sumar k y restar k en modulo 26 se cancelan: se recupera x. La fuerza bruta es posible porque solo hay 26 claves; se pueden generar todas las salidas y reconocer el mensaje en español a ojo.

### Como se ejecuta
```text
python tests/Criptograf/test_cs.py
```

### Pruebas
- HOLA UNAL con k=3 da KROD XQDO.
- SOLO DISCRETAS y ESPAÑA CAMPEON (la ñ se deja igual porque no esta en A..Z).
- Fuerza bruta sobre el cifrado del ejemplo 1: aparece el original en k=3.

### Limitaciones
No es seguro. Conserva longitud y patrones del texto. Solo mueve letras latinas; numeros, espacios y signos no cambian.


## 2. RSA de juguete

### Que problema resuelve
Generar llaves a partir de dos primos p, q y un exponente e, cifrar un mensaje entero M y recuperarlo.

### Idea matematica
Se calcula n=pq y $\phi (n)$=(p-1)(q-1). El exponente privado d es el inverso modular de e modulo φ(n), o sea

ed ≡ 1 (mod $\phi (n)$).

Eso se obtiene con el algoritmo de Euclides extendido. Cifrado y descifrado:

$$
C \equiv M^{e} \pmod{n}, \qquad M \equiv C^{d} \pmod{n}.
$$

Los primos hacen dificil factorizar n (en tamaños reales de producción en la industra, extremadamente grandes). Aqui n es pequeño a proposito.

### Para la documentacion
p y q son primos porque asi n=pq tiene exactamente esos dos factores no triviales, y $\phi (n)$=(p-1)(q-1) se calcula con facilidad si se conocen p y q, pero es dificil de obtener si solo se ve n. El inverso modular d existe solo cuando gcd(e, $\phi(n)$)=1; ese d es la llave privada que “deshace” la potencia e. La congruencia funciona, pues todo el cifrado vive en aritmetica modulo n: elevar a e y luego a d no es una resta ordinaria, sino una operacion que, gracias a ed ≡ 1 (mod $\phi$(n)) y al teorema de Euler, recupera M modulo n.

### Como se ejecuta
```text
python tests/Criptograf/test_rsa.py
```

### Pruebas
Caso obligatorio: p=61, q=53, e=17, M=65 -> n=3233, $\phi (n)$=3120, d=2753, C=2790, y al descifrar vuelve 65. Tambien se prueba un e invalido con gcd(e, $\phi (n)$) ≠ 1.

### Limitaciones
No es RSA real. No hay padding, los primos son diminutos y el mensaje es un entero < n. 


## 3. MPC basico (promedio sin revelar notas)

### Que problema resuelve
Calcular la suma y el promedio de varias notas sin que un solo servidor vea la lista original.

### Idea matematica
Cada nota se reparte en tres partes modulo M. Cada servidor suma solo lo suyo; al juntar las tres sumas locales se obtiene la suma total y el promedio.

x ≡ s1 + s2 + s3 (mod M).

Una sola parte no determina x (hay muchas formas de completar la suma). Cada servidor solo suma lo que le corresponde; al juntar las tres sumas locales se recupera la suma total de las notas, y de ahi el promedio.

### Para la documentacion
Ejemplo chico. Sea x = 40 y M = 100. Se eligen al azar s1 = 17 y s2 = 55; entonces s3 = (40 - 17 - 55) mod 100 = 68. Chequeo: 17 + 55 + 68 = 140 ≡ 40 (mod 100). Si alguien solo ve s1 = 17, no sabe x: podria ser 17+0+23, o 17+10+13, etc. Hacen falta las tres partes (o dos, si se conoce el modulo y se colude) para reconstruir la nota.

### Como se ejecuta
```text
python tests/Criptograf/test_mpc.py
```

### Pruebas
Con notas [40, 35, 50, 25] se obtiene suma 150 y promedio 37.5. Se muestran las partes que ve cada servidor y un chequeo de que s1 + s2 + s3 ≡ x (mod M).

### Limitaciones
Es una simulacion, no un protocolo de producción. Si dos servidores se coluden pueden reconstruir mas informacion. M tiene que ser mayor que la suma esperada.


## 4. Ruta mas corta (Dijkstra)

### Que problema resuelve
Encontrar el camino de menor costo entre dos estaciones de un grafo ponderado con pesos positivos.

### Idea matematica
Dijkstra mantiene distancias tentativas y siempre expande el vertice pendiente con menor distancia conocida. Con pesos $\ge 0$ esa eleccion es segura: la primera vez que se llega a el destino, su distancia ya es optima. Si hubiera pesos negativos, esa garantia se rompe.

### Para la documentacion
Necesita pesos no negativos porque la prueba de optimalidad asume que al sacar un vertice su distancia ya no puede mejorar: con un peso negativo eso falla. Un camino es optimo si no existe otro entre el mismo origen y destino con costo estrictamente menor.

### Como se ejecuta
```text
python tests/Grafos/test_ruta_corta.py
```

El grafo se carga desde la lista de aristas (a, b, peso) en `src/Grafos/ruta_corta.py`.

### Pruebas
9 vertices y mas de 12 aristas. Ejemplos: Portal→Aeropuerto, Museo→Usaquen, Calle26→Chapinero (distancia y ruta).

### Limitaciones
No admite pesos negativos. El grafo de prueba es no dirigido (cada arista se mete en ambos sentidos). La implementacion es la clasica $O(V^2)$, suficiente para grafos chicos.


## 5. Cierre de una estacion

### Que problema resuelve
Ver como cambian las rutas mas cortas si se elimina un vertice: cuales se alargan y cuales se desconectan.

### Idea matematica
Se recalculan rutas mas cortas (Dijkstra) antes y despues de quitar el vertice y sus aristas. La diferencia de distancias cuantifica el impacto. Si despues no hay camino, el par queda desconectado.

### Para la documentacion
Se cerraron tres estaciones distintas para ver el contraste. Chapinero es un nodo central: varias rutas pasan por ahi, asi que la mayoria de pares empeoran o se desconectan. Calle26 solo afecta una direccion concreta (Portal->Aeropuerto sube un poco). Soacha es periferica y no entra en las rutas de prueba, asi que el cierre no mueve nada en esos pares. El impacto importa porque muestra que no todo cierre “rompe” la red igual: depende de que tan puente sea el vertice.

### Como se ejecuta
```text
python tests/Grafos/test_cierre_estacion.py
```

### Pruebas
Seis pares origen-destino. Para cada cierre: tabla completa y clasificacion (aumentaron / iguales / desconectados).

### Limitaciones
Solo modela cierre de vertice, no de una arista suelta. El impacto depende de los pares que uno elija mirar; un nodo “inocente” para esos pares podria ser critico para otros.

## 6. Coloreo de grafos

### Que problema resuelve
Asignar franjas horarias a cursos de forma que dos cursos con estudiantes en comun no queden en la misma franja.

### Idea matematica
Grafo de conflictos: vertice = curso, arista = estudiantes en comun. Cada color es una franja. El algoritmo voraz recorre los vertices y pone el menor color libre respecto a los vecinos.

### Para la documentacion
El voraz siempre da un coloreo valido (ningun adyacente comparte color) si se implementa bien, pero no garantiza el minimo posible de colores: el numero de colores usados puede ser menor. El orden de los vertices cambia cuantas franjas salen; por eso dos ordenes distintos pueden usar mas o menos colores aunque ambos sean correctos.

### Como se ejecuta
```text
python tests/Grafos/test_coloreo.py
```

### Pruebas
Grafo con 11 cursos y 20 conflictos. Se colorea con dos ordenes distintos, se cuenta cuantos colores salen y se verifica que no hay adyacentes del mismo color.

### Limitaciones
No busca el optimo global de franjas. Busca una asignación válida y depende del orden.


## 7. Tablas de verdad

### Que problema resuelve
Evaluar expresiones booleanas con AND, OR, NOT y XOR sobre A, B, C, D: tabla completa y evaluacion de una entrada.

### Idea matematica
Una tabla de verdad lista todas las asignaciones de las variables (2^n filas) y el valor de la expresion. Eso es exactamente lo que describe el comportamiento de un circuito logico: cada fila es una combinacion de entradas y la columna de salida es lo que produce el circuito.

### Para la documentacion
La tabla de verdad es el “manual” del circuito: cada fila es una combinacion de entradas (voltajes altos/bajos) y la columna final es lo que produce el circuito con esas compuertas. Si dos circuitos tienen la misma tabla, se comportan igual aunque se armen distinto.

### Como se ejecuta
```text
python tests/Boole/test_tablas_verdad.py
```

### Pruebas
Las tres expresiones del enunciado (16 filas). Tambien una expresion propia: (A OR B) AND (C XOR D).

### Limitaciones
Las expresiones estan definidas como funciones en Python, no como un parser de strings. Si se quiere otra formula hay que escribir otra funcion. Con muchas variables la tabla crece exponencialmente.

## 8. Simplificacion booleana

### Que problema resuelve
Partir de los minterminos de una funcion y obtener una expresion mas corta en forma suma de productos, comprobando que la tabla no cambia.

### Idea matematica
Un mintermino es un producto que vale 1 en exactamente una fila de la tabla. Quine-McCluskey agrupa terminos que difieren en un bit y reemplaza ese bit por “no importa” (-), hasta obtener implicantes primos; despues se elige un cubrimiento. Dos expresiones son equivalentes si inducen la misma funcion $\{0,1\}^n \to \{0,1\}$, es decir la misma tabla.

### Para la documentacion
Un mintermino es el producto que vale 1 en una sola fila de la tabla (por ejemplo, para tres variables, el mintermino 5 corresponde a la fila 101). Dos expresiones son equivalentes si dan la misma salida en todas las filas, o sea si tienen la misma tabla de verdad: da igual como se escriban si la funcion {0,1}^n → {0,1} es la misma.

### Como se ejecuta
```text
python tests/Boole/test_simplificacion.py
```

### Pruebas
- $[1,3,5,7] -> C$
- $[0,2,4,6] -> C'$
- $[0,1,8,9] -> B'C'$
En todos los casos se marca Tablas iguales: True.

### Limitaciones
Version pequeña pensada para 3 o 4 variables. No usa librerias de algebra simbolica: la verificacion es propia, comparando fila a fila. El cubrimiento greedy no siempre da el conjunto minimo absoluto de implicantes, aunque en los ejemplos del taller si llega a la forma esperada.

## 9. Entropia de Shannon

### Que problema resuelve
Medir que tan incierto es un texto a partir de sus simbolos, comparar dos mensajes y (extension) contrastar con la longitud promedio de un codigo Huffman.

### Idea matematica
Con p_i = frecuencia relativa del simbolo i, H = $-\Sigma p_i · \log_2 (p_i).$ Huffman construye un codigo prefijo y se compara L con H.

### Para la documentacion
La entropia no mide “que tan largo es el texto”, sino que tan impredecible es el siguiente simbolo. Un mensaje de diez aes tiene longitud 10 pero H = 0: no hay sorpresa. Otro mas corto pero con letras mezcladas puede tener H mayor porque hay mas incertidumbre por caracter.

### Como se ejecuta
```text
python tests/Cuantica/test_shannon.py
```

### Pruebas
Texto repetitivo "aaaaaaaaaa" (H=0) contra "matematicas discretas" (H mayor). El programa indica cual gana y por que. Ademas se construye un codigo Huffman y se compara la longitud promedio L con H (en el texto variado, L queda apenas por encima de H).

### Limitaciones
Se toma cada caracter como simbolo (incluyendo espacios). La entropia empirica depende del texto concreto, no estima una fuente infinita. Huffman da un codigo prefijo cuya longitud promedio L cumple $H \le L < H+1$ en la practica del ejemplo; con un solo simbolo distinto, L=1 aunque H=0.

## 10. Simulador de un qubit

### Que problema resuelve
Representar un qubit como vector de dos amplitudes, aplicar X, Z y H, calcular P(0), P(1) y simular mediciones.

### Idea matematica
El estado es $\alpha|0\rangle + \beta|1\rangle$ con $|\alpha|^2+|\beta|^2=1$. Las compuertas son matrices 2 x 2 que actuan por multiplicacion.

### Para la documentacion
Aqui la “probabilidad cuantica” se calcula en la CPU a partir del vector de estado y despues se simulan tiros aleatorios. En un computador cuantico real no se lee el vector: solo se miden bits 0/1, con ruido y decoherencia, y hace falta repetir el experimento muchas veces. La simulacion es util para entender X, H y HH, pero no es lo mismo que ejecutar en el hardware adecuado.

### Como se ejecuta
```text
python tests/Cuantica/test_qubit.py
```

### Pruebas
X|0> = |1>; H|0> cerca de 50/50 en 1000 mediciones; HH|0> = |0>. Extra: Z|0>.

### Limitaciones
Un solo qubit, amplitudes reales en la practica de estos ejemplos, sin ruido. No escala a circuitos grandes; es solo para ver la idea.

## Nota final

Si algo no corre, lo primero es confirmar que la terminal esta en la raiz del repo y que el comando es `python` (o `py`). Los detalles de ejecucion tambien estan en el `README.md`.

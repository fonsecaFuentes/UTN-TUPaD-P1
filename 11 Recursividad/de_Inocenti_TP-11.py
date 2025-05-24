"""
1-Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario
"""
def factorial(num):
    # Caso base
    if num == 0:
        return 1
    else:
        # Paso recursivo
        return num * factorial(num-1)

# Demostración del factorial
n = int(input("[Factorial] Ingrese un número entero no negativo: "))
print(f"Factoriales desde 0 hasta {n}:")
for i in range(n + 1):
    print(f"  {i} = {factorial(i)}")

"""
2-Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique.
"""

def fibonacci(pos):
    # Caso base
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    # Paso recursivo
    else:
        return fibonacci(pos-1) + fibonacci(pos-2)

# Demostración de Fibonacci
m = int(input("\n[Fibonacci] Ingrese la posición máxima: "))
print(f"Serie de Fibonacci hasta F({m}):")
for i in range(m + 1):
    print(f"  F({i}) = {fibonacci(i)}")

"""
3-Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula 𝑛𝑚 = 𝑛∗𝑛(𝑚−1). Prueba esta función en un
algoritmo general
"""

def potencia(base, exponente):
    # Caso base
    if exponente == 0:
        return 1
    elif exponente > 0:
        # Exponente positivo
        return base * potencia(base, exponente-1)
    else:
        # Exponente negativo: invertir
        return 1 / potencia(base, -exponente)

# Demostración de la potencia
b = int(input("\n[Potencia] Introduce la base: "))
e = int(input("[Potencia] Introduce el exponente: "))
print(f"{b}^{e} = {potencia(b, e)}")

"""
4-Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto
"""

def decimal_a_binario(num):
    # Caso base
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    else:
        # Paso recursivo:
        return decimal_a_binario(num//2) + str(num % 2)

# Demostración de la conversión a binario
x = int(input("\n[Binario] Introduce un entero no negativo: "))
print(f"  {x} en binario es {decimal_a_binario(x)}")

"""
5-Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.
Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed()
"""

def es_palindromo(palabra):
    # Caso base:
    if len(palabra) <= 1:
        return True
    # Si extremos difieren, no es palíndromo
    if palabra[0] != palabra[-1]:
        return False
    # Paso recursivo
    return es_palindromo(palabra[1:-1])

# Demostración de palíndromos
ejemplos = [
        "radar",
        "reconocer",
        "palabra",
        "python",
    ]
print("\n[Palíndromo] Ejemplos:")
for palabra in ejemplos:
    print(f"La palabra {palabra} es palindromo? {es_palindromo(palabra)}")

"""
6-Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.
Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
Ejemplos:
suma_digitos(1234)   → 10  (1 + 2 + 3 + 4)
suma_digitos(9)      → 9
suma_digitos(305)    → 8   (3 + 0 + 5)
"""

def suma_digitos(n):
    # Caso base
    if n < 10:
        return n
    else:
        # Paso recursivo
        return (n % 10) + suma_digitos(n // 10)

# Demostración de suma de dígitos
ejemplos = [1234, 9, 305, 0]
print("\n[Suma Dígitos] Ejemplos:")
for num in ejemplos:
    print(f"La suma de los digitos {num} es: {suma_digitos(num)}")

"""
7-Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.

Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.

Ejemplos:
contar_bloques(1)   → 1         (1)
contar_bloques(2)   → 3         (2 + 1)
contar_bloques(4)   → 10        (4 + 3 + 2 + 1)
"""

def contar_bloques(n):
    # Caso base
    if n == 1:
        return 1
    else:
        # Paso recursivo
        return n + contar_bloques(n-1)

# Demostración de contar bloques
bloques = [1, 2, 3, 4, 10]
print("\n[Contar Bloques] Ejemplos:")
for x in bloques:
    print(f"Para {x} bloques en el primer nivel, necesita {contar_bloques(x)} bloques en total")

"""
8-Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.
Ejemplos:
contar_digito(12233421, 2)   → 3
contar_digito(5555, 5)       → 4
contar_digito(123456, 7)     → 0
"""

def contar_digito(numero, digito):
    # Caso base
    if numero < 10:
        if numero == digito:
            return 1
        else:
            return 0
    # Contar en el último dígito y sumar recursión en el resto
    elif numero % 10 == digito:
        actual = 1
    else:
        actual = 0
    return actual + contar_digito(numero // 10, digito)

# Demostración de contar dígitos
ejemplos = [
        (12233421, 2),
        (5555, 5),
        (123456, 7),
        (70707, 0),
    ]
print("\n[Contar Dígito] Ejemplos:")
for num, dig in ejemplos:
    print(f"{num}, {dig} = {contar_digito(num, dig)}")
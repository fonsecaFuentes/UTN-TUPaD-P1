import math
import random
"""
1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
"""
print("Ejercicio 1:")
for n in range(101):
    print(n)

"""
2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene.
"""
print("\nEjercicio 2:")
num_usuario = int(input("Introduce un número entero: "))

cont = 0

while num_usuario >= 1:
    num_usuario /= 10
    cont += 1

print(f"El número ingresado tiene {cont} dígitos")

"""
3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.
"""
print("\nEjercicio 3:")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
acum= 0

for n in range(num1 + 1, num2):
    acum += n

print(f"La suma de los números comprendidos entre los dos valores dados es {acum}")

"""
4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
"""
print("\nEjercicio 4:")
acum = 0
num_ingresado = int(input("Ingrese un número (0 para finalizar): "))

while num_ingresado != 0:
    acum += num_ingresado
    num_ingresado = int(input("Ingrese otro número (0 para finalizar): "))

print(f"La suma de las números ingresados es {acum}")

"""
5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
"""
print("\nEjercicio 5:")
numero_aleatorio = random.randint(0, 9)
intentos = 1
bandera = True

print("Se ha generado un número aleatorio entre 0 y 9.")
print("Adivina cuántos intentos te llevará acertar el número.")

while bandera:
    num_usuario = int(input(f"Intento número {intentos}: "))
    if num_usuario == numero_aleatorio:
        print(f"Acertaste!! Cantidad de intentos {intentos}")
        bandera = False
    else:
        print("Incorrecto, intenta de nuevo")
        intentos += 1

"""
6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente.
"""
print("\nEjercicio 6:")
for x in range(100, -1, -2):
    print(x)

"""
7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.
"""
print("\nEjercicio 7:")
num = int(input("Ingrese un número entero positivo: "))
acum = 0

# Validamos que el número sea positivo.
while num <= 0:
    num = int(input("Por favor, ingrese un número entero positivo: "))

for x in range(0, num + 1):
    acum += x

print(f"La suma de todos los números comprendidos entre 0 y {num} es: {acum}")
"""
8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).
"""
print("\nEjercicio 8:")
TOTAL = 100
pares = 0
impares = 0
positivos = 0
negativos = 0

for n in range(TOTAL):
    num = int(input(f"Ingrese el primer número ({n+1}): "))
    # números pares e impares
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    # números negativos y positivos
    if num < 0:
        negativos += 1
    elif num > 0:
        positivos += 1

print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números negativos:", negativos)
print("Cantidad de números positivos:", positivos)

"""
9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).
"""
print("\nEjercicio 9:")
TOTAL_NUM = 100
acum = 0

for x in range(TOTAL_NUM):
    num_user = int(input(f"Ingrese el primer número ({x+1}): "))
    acum += num_user

media = acum / TOTAL_NUM

print(f"La media de los números ingresados es {media}")
"""
10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
"""
print("\nEjercicio 10:")
num = int(input("Ingrese un número: "))
num_invertido = 0

while num > 0:
    # Extraemos el último dígito
    digito = num % 10

    # Se Construye el número invertido
    num_invertido = num_invertido * 10
    num_invertido += digito

    # Eliminamos el último dígito del número original
    num = math.trunc(num / 10)

print(f"Al invertir los dígitos del número ingresado se obtiene: {num_invertido}")
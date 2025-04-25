import math

# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")

"""
2) Crear un programa que pida al usuario su nombre e imprima por pantalla un
saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”,
el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más
sencillo si utilizas print(f…) para realizar la impresión por pantalla.
"""

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}")

"""
3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de
residencia e imprima por pantalla una oración con los datos ingresados.
Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”,
el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en
Argentina”. Consejo: esto será más sencillo si utilizas print(f…)
para realizar la impresión por pantalla.
"""

nombre_completo = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar_residencia = input("Su lugar de residencia?: ")

print(f"Soy {nombre_completo} {apellido}, "
      f"tengo {edad} años y vivo en {lugar_residencia}")

"""
4) Crear un programa que pida al usuario el radio de un círculo e imprima
por pantalla su área y su perímetro."
"""

radio = float(input("Ingrese el radio del círculo: "))

area = round(math.pi * (radio) ** 2, 2)
perimetro = round(2 * math.pi * radio, 2)

print(f"El área del círculo es: {area} y su périmetro es: {perimetro}")

"""
5) Crear un programa que pida al usuario una cantidad de segundos e imprima
por pantalla a cuántas horas equivale.
"""

segundos = int(input("Ingrese una cantidad x de segundos: "))
horas = round(segundos / 3600, 2)

print(f"{segundos} segundos es igual a {horas} hora/s")

"""
6) Crear un programa que pida al usuario un número e imprima por pantalla
la tabla de multiplicar de dicho número.
"""

numero = int(input("Ingrese un número: "))
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

"""
7) Crear un programa que pida al usuario dos números enteros distintos del 0 y
muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y
restarlos.
"""

numero1 = int(input("Ingrese un número entero distinto del 0: "))
numero2 = int(input("Ingrese un segundo número entero distinto del 0: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(f"La suma entre {numero1} y {numero2} es {suma}")
print(f"La resta entre {numero1} y {numero2} es {resta}")
print(f"La multiplicación entre {numero1} y {numero2} es {multiplicacion}")
print(f"La división entre {numero1} y {numero2} es {division}")

"""
8) Crear un programa que pida al usuario su altura y su peso e imprima por
pantalla su índice de masa corporal. Tener en cuenta que el índice de masa
corporal se calcula del siguiente
modo:

I𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔
     (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2
"""

peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))

masa_corporal = peso / (altura ** 2)

print(f"Con un peso de {peso} kg y una altura de {altura} m, "
      f"su índice de masa corporal es: {masa_corporal}")

"""
9) Crear un programa que pida al usuario una temperatura en grados Celsius
e imprima por pantalla su equivalente en grados Fahrenheit.
Tener en cuenta la siguiente equivalencia:

t𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5.𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
"""

grados_celsius = float(input("Ingrese una temperatura en grados Celsius: "))
grados_fahrenheit = (9/5 * grados_celsius) + 32

print(f"El equivalente en {grados_celsius} grados Celsius a grados Fahrenheit "
      f"es {grados_fahrenheit}")

"""
10) Crear un programa que pida al usuario  3 números e imprima por pantalla
el promedio de dichos números.
"""

prom_numero1 = float(input("Ingrese el primer número: "))
prom_numero2 = float(input("Ingrese el segundo número: "))
prom_numero3 = float(input("Ingrese el tercer número: "))

promedio = (prom_numero1 + prom_numero2 + prom_numero3) / 3
print(f"El promedio de los números: {prom_numero1}, {prom_numero2} y "
      f"{prom_numero3} es {promedio}")

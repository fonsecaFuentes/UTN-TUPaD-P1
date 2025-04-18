import math
import utils

"""
1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal.
"""
print("Actividad 1\n")

# Definicion de funciones
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Programa principal
imprimir_hola_mundo()

print("###########################################################\n")
"""
2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario('Marcos'), deberá de-
volver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario.
"""
print("Actividad 2\n")

# Definicion de funciones
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

# Programa principal
nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)

print("###########################################################\n")
"""
3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe-
dir los datos al usuario y llamar a esta función con los valores in-
gresados.
"""
print("Actividad 3\n")

# Definicion de funciones
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Programa principal
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad_float = utils.validar_num("Ingrese su edad", 1)
edad = int(edad_float)
residencia = input("Ingrese su residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

print("###########################################################\n")
"""
4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra-
dio como parámetro y devuelva el área del círculo. calcular_peri-
metro_circulo(radio) que reciba el radio como parámetro y devuel-
va el perímetro del círculo. Solicitar el radio al usuario y llamar am-
bas funciones para mostrar los resultados.
"""
print("Actividad 4\n")

# Definicion de funciones
def calcular_area_circulo(radio):
    area = round((math.pi * (radio ** 2)), 2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = round((2 * math.pi * radio), 2)
    return perimetro

# Programa principal
r = utils.validar_num("Ingrese el radio del círculo", 1)

area = calcular_area_circulo(r)
perimetro = calcular_perimetro_circulo(r)

print(f"El área del círculo de radio {r} es: {area}")
print(f"El perímetro del círculo de radio {r} es: {perimetro}")

print("###########################################################\n")
"""
5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mos-
trar el resultado usando esta función.
"""
print("Actividad 5\n")

# Definicion de funciones
def segundos_a_horas(segundos):
    horas = round((segundos / 3600), 2)
    return horas

# Programa principal
s = utils.validar_num("Ingrese la cantidad de segundos", 0)
resultado = segundos_a_horas(s)

print(f"{s} segundos equivalen a {resultado} horas")

print("###########################################################\n")
"""
6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la fun-
ción.
"""
print("Actividad 6\n")

# Definicion de funciones
def mostrar_tabla(num1, num2):
    print(f"{num1} x {num2} = {num1 * num2}")

def tabla_multiplicar(numero):
    for i in range(11):
        mostrar_tabla(numero, i)

# Programa principal
num_float = utils.validar_num("Ingrese un numero", 1)
num_int = int(num_float)
tabla_multiplicar(num_int)

print("###########################################################\n")
"""
7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado
de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los
resultados de forma clara.
"""
print("Actividad 7\n")

# Definicion de funcionesasd
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = round((a / b), 2)
    else:
        division = None
    return (suma, resta, multiplicacion, division)

# Programa principal
x = float(input("Ingrese el primer número (a): "))
y = float(input("Ingrese el segundo número (b): "))

suma, resta, producto, division = operaciones_basicas(x, y)

print(f"\nResultados para a = {x} y b = {y}:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {producto}")
if division is not None:
    print(f"División: {division}")
else:
    print(f"División: Error (división por cero)")

print("###########################################################\n")
"""
8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun-
ción para mostrar el resultado con dos decimales.
"""
print("Actividad 8\n")

# Definicion de funciones
def calcular_imc(peso, altura):
    resultado = peso / (altura ** 2)
    return resultado

# Programa principal
peso = utils.validar_num("Ingrese su peso", 1)
altura = utils.validar_num("Ingrese su altura", 1)

imc = calcular_imc(peso, altura)

print(f"Con un peso de {peso} y una altura de {altura} su IMC es de {round(imc, 2)}")

print("###########################################################\n")
"""
9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.
"""
print("Actividad 9\n")

# Definicion de funciones
def celsius_a_fahrenheit(celsius):
    resultado = round(((9/5 * celsius) + 32), 2)
    return resultado

# Programa principal
grados_celsius = int(input("Ingrese una temperatura en grados Celsius: "))
grados_fahrenheit = celsius_a_fahrenheit(grados_celsius)

print(f"El equivalente en {grados_celsius} grados Celsius a grados Fahrenheit es {grados_fahrenheit}")

print("###########################################################\n")
"""
10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.
"""
print("Actividad 10\n")

# Definicion de funciones
def calcular_promedio(a, b, c):
    promedio = round(((a + b + c) / 3), 2)
    return promedio

# Programa principal
num1 = utils.validar_num("Ingrese el primer parámetro", 1)
num2 = utils.validar_num("Ingrese el segundo parámetro", 1)
num3 = utils.validar_num("Ingrese el tercer parámetro", 1)

promedio = calcular_promedio(num1, num2, num3)

print(f"El promedio de los parámetros {num1}, {num2} y {num3} es {promedio}")
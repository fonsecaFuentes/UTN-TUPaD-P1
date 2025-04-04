from statistics import mode, median, mean
import random
# Práctico 3: Estructuras condicionales

# Actividades
"""
1) Escribir un programa que solicite la edad del usuario.
Si el usuario es mayor de 18 años, deberá mostrar un mensaje
en pantalla que diga “Es mayor de edad”.
"""
# Pedir por consola la edad del usuario
edad = int(input("Ingrese su edad: "))

# Comparamos si la edad es mayor que 18 o no
if edad > 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")

"""
2) Escribir un programa que solicite su nota al usuario.
Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje
que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.
"""
# Pedir por consola la nota del usuario
nota = int(input("Ingrese su nota: "))

# Evaluamos si la nota es mayor igual que 6
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

"""
3) Escribir un programa que permita ingresar solo números pares.
Si el usuario ingresa un número par, imprimir por en pantalla el mensaje
"Ha ingresado un número par"; en caso contrario, imprimir por pantalla
"Por favor, ingrese un número par". Nota: investigar el uso del operador
de módulo (%) en Python para evaluar si un número es par o impar.
"""

# Pedimos por consola un número al usuario
numero = int(input("Ingrese un número: "))

# Evaluamos si es par o impar
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

"""
4) Escribir un programa que solicite al usuario su edad e imprima
por pantalla a cuál de las siguientes categorías pertenece:
    ● Niño/a: menor de 12 años.
    ● Adolescente: mayor o igual que 12 años y menor que 18 años.
    ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
    ● Adulto/a: mayor o igual que 30 años.
"""

# Pedir por consola la edad del usuario
edad = int(input("Ingrese su edad: "))

# Evaluamos la edad del usuario
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

"""
5) Escribir un programa que permita introducir contraseñas de entre
8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña
de longitud adecuada, imprimir por en pantalla el mensaje
"Ha ingresado una contraseña correcta"; en caso contrario,
imprimir por pantalla "Por favor, ingrese una contraseña de entre
8 y 14 caracteres". Nota: investigue el uso de la función len() en Python
para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string.
"""

# Pedimos al usuario que ingrese una contraseña
password = input("Ingrese una contraseña entre 8 y 14 caracteres: ")

# Contamos cuantos caracteres tiene la contraseña ingresada por el usuario
caracteres = len(password)

# Se valida si la contraseña cumple con los requisitos
if caracteres >= 8 and caracteres <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

"""
6) El paquete statistics de python contiene funciones que permiten tomar una
lista de números y calcular la moda, la mediana y la media de dichos números.
Un ejemplo de su uso es el siguiente:
    from statistics import mode, median, mean
    mi_lista = [1,2,5,5,3]
    mean(mi_lista)
En la documentación oficial se puede encontrar más información sobre este
paquete: https://docs.python.org/es/3.8/library/statistics.html.
La moda (mode), la mediana (median) y la media (mean) son parámetros
estadísticos que se pueden utilizar para predecir la forma de una
distribución normal a partir del siguiente criterio:
    ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana
    y, a su vez, la mediana es mayor que la moda.
    ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana
    y, a su vez, la mediana es menor que la moda.
    ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para
determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el
resultado por pantalla. Definir la lista numeros_aleatorios de
la siguiente forma:
    import random
    numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100
elegidos de forma aleatoria.
"""

# Generamos números aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calculamos moda, mediana y media
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

# Mostramos por consola los valores de moda, mediana y media
print(media)
print(mediana)
print(moda)
print("")

# Comparamos para definir definir el sesgo
if media > mediana > moda:
    print("Sesgo positivo")
elif media < mediana < moda:
    print("Sesgo negativo")
elif media == mediana == moda:
    print("No hay sesgo")
else:
    print(
        "la relación entre media, la mediana y"
        " la moda no sigue un patron de sesgo definido"
        )

"""
7) Escribir un programa que solicite una frase o palabra al usuario.
Si el string ingresado termina con vocal, añadir un signo de exclamación
al final e imprimir el string resultante por pantalla; en caso contrario,
dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
"""

# Pedimos cpor consola al usuario que ingrese una palabra o frase
entrada_usuario = input("Ingrese una frase o palabra: ")

# Verificamos la ultima letra si es una vocal
if entrada_usuario[-1] in "aeiou":
    resultado = entrada_usuario + "!"
else:
    resultado = entrada_usuario

# Mostramos el resultado
print(resultado)


"""
8) Escribir un programa que solicite al usuario que ingrese su nombre
y el número 1, 2 o 3 dependiendo de la opción que desee:
    1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
    2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
    3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción
seleccionada por el usuario e imprimir el resultado por pantalla.
Nota: investigue uso de las funciones upper(), lower() y title() de
Python para convertir entre mayúsculas y minúsculas.
"""

# Pedimos por consola el nombre del usuario
nombre = input("Ingrese su nombre: ")
# Pedimos al usuario que elija una opción
opcion = int(
            input(
                "Elija una opción:\n"
                "1. Si quiere su nombre en mayúsculas.\n"
                "2. Si quiere su nombre en minúsculas.\n"
                "3. Si quiere su nombre con la primera letra mayúscula.\n"
                "Opción: "
            )
            )

# Validamos la opción
if opcion == 1:
    nombre = nombre.upper()
elif opcion == 2:
    nombre = nombre.lower()
elif opcion == 3:
    nombre = nombre.title()
else:
    nombre = "La opción selecionada no corresponde, elija opcion 1, 2 o 3"

# Mostramos por pantalla el resultado
print(nombre)

"""
9) Escribir un programa que pida al usuario la magnitud de un terremoto,
clasifique la magnitud en una de las siguientes categorías según la escala
de Richter e imprima el resultado por pantalla:
    ● Menor que 3: "Muy leve" (imperceptible).
    ● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible).
    ● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas,
    pero generalmente no causa daños).
    ● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños
    en estructuras débiles).
    ● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar
    daños significativos).
    ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
"""

# Pedimos por consola datos al usuario
escala_richter = int(
    input(
        "Ingrese la escala del terremoto(segun escala de Richter): "
        )
    )

# Evaluamos el dato proporcionado por el usuario
if escala_richter < 3:
    clasificacion = "'Muy leve' (imperceptible)."
elif escala_richter >= 3 and escala_richter < 4:
    clasificacion = "'Leve' (ligeramente perceptible)"
elif escala_richter >= 4 and escala_richter < 5:
    clasificacion = "'Moderado' (sentido por personas,"
    " pero generalmente no causa daños)"
elif escala_richter >= 5 and escala_richter < 6:
    clasificacion = "'Fuerte' (puede causar daños en estructuras débiles)"
elif escala_richter >= 6 and escala_richter < 7:
    clasificacion = "'Muy Fuerte' (puede causar daños significativos)"
else:
    clasificacion = "'Extremo' (puede causar graves daños a gran escala)"

# Mostramos el resultado por consola
print(clasificacion)

"""
10) Escribir un programa que pregunte al usuario en cuál hemisferio se
encuentra (N/S), qué mes del año es y qué día es. El programa deberá
utilizar esa información para imprimir por pantalla si el usuario se
encuentra en otoño, invierno, primavera o verano.
"""
# Solicitamos datos al usuario
hemisferio = input("En que hemisferio se encuentra? (Ingrese N para norte o S para sur): ").upper()
mes = int(input("Ingrese el mes del año (en número): "))
dia = int(input("Ingrese el dia (en número): "))

# Determinamos que hemisferio se encuentra el usuario
if hemisferio == "S":
    # Si es hemisferio sur
    if (mes == 3 and dia >= 21) or (mes > 3 and mes < 6) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes > 6 and mes < 9) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes > 9 and mes < 12) or (mes == 12 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 12 and dia >= 21) or (mes >= 1 and mes <= 2) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    else:
        estacion = "Fecha inválida"

elif hemisferio == "N":
    # Si es hemisferio norte
    if (mes == 9 and dia >= 21) or (mes > 9 and mes < 12) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 12 and dia >= 21) or (mes >= 1 and mes <= 2) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes > 3 and mes < 6) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes > 6 and mes < 9) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    else:
        estacion = "Fecha inválida"

# Mostramos el resultado
print(estacion)
# Operaciones Básicas: 
#1) Realiza la suma, resta, multiplicación y división de dos números ingresados por el usuario.
#Datos de entrada
num1= int(input("Ingrese el primer número:"))
num2= int(input("Ingrese el segundo número:"))
#operaciones
suma = num1 + num2
resta = num1 - num2
producto = num1 * num2
division = num1 / num2
#mostrando resultados
print("la suma de los números ingresados es:",suma)
print("la resta de los números ingresados es:",resta)
print("la multiplicación de los números ingresados es:",producto)
print("la división de los números ingresados es:",division)

# Verificación de Número Par o Impar:
#2) Solicita un número al usuario y determina si es par o impar. 
#Dato de entrada
num = int(input("Ingrese un número:"))
#Condición para determinar si el dato de entrada es par o impar
if num % 2 == 0:
    print("El número ",num," es PAR")
else:
    print("El número ",num," es IMPAR")

# Área de un Triángulo: 
# 3) Pide la base y la altura de un triángulo al usuario y calcula su área.
#Datos de entrada
base = int(input("Ingrese la base del triángulo: "))
altura = int(input("Ingrese la altura del triángulo: "))
#Operación para calcular el área
area = (base*altura)/2
#Mostrar dato
print("El área del triángulo es:",area)

# Calculadora de Factorial: 
# 4) Crea una función que calcule la factorial de un número. 
#Dato de entrada
num = int(input("Ingrese un número: "))
#Inicializando variables
fact = 1
i = 1
#Iteración de los factores
while (i <= num):
    fact = fact * i
    i += 1
#Mostrar el resultado
print("El factorial de ",num," es: ",fact)

#Número Primo: 
# 5) Verifica si un número ingresado por el usuario es primo o no
#Datos de entrada
num = int(input("Ingrese un número: "))
#Iteración desde 2 hasta el número ingresado para verificar mediante su modulo si es primo o no
for i  in range(2,num):
    if num % i == 0:
        print("El número ",num," NO ES PRIMO")
        break
    print("El número ",num," ES PRIMO")
    break

# Inversión de Cadena: 
# 6) Toma una cadena de texto y muestra su inversión. 
#Dato de entrada
txt = str(input("Ingrese un texto: "))
#Mostrar datos
print("El inverso del texto ingresado es: ",txt[::-1])

# Suma de Números Pares: 
# 7) Calcula la suma de los números pares en un rango especificado por el usuario. 
#Ingreso del rango para sumar los números pares
rango = int(input("Ingrese un rango: "))

#Inicializando variable sum
sum = 0
#iteración para verificar si los números dentro de ese rango son pares verificando su modulo
for i in range (2,rango+1):
    if i%2==0:
        sum +=i
        print(i)
#Muestra del resultado
print("La suma de los números pares de 0 HASTA ",rango," es: ",sum)

# Lista de Cuadrados: 
# 8) Crea una lista de los cuadrados de los primeros 10 números naturales.
#Iniciamos la variable en una lista vacia
cuadrados = list()
#Iteración del 1 al 11 para luego agregar el cuadrado de cada número en la lista
for i in range (1,11):
    cuadrados.append(i*i)
#Mostrar resultado
print("La lista de los cuadrados de los 10 primeros números es: ",cuadrados)

# Contador de Vocales: 
# 9) Cuenta el número de vocales en una cadena de texto. 
#Ingreso de dato
txt = str(input("Ingresa un texto: "))
#Asignando una cadena estática de las vocales e inicializando el contador
vocales = "aeiouáéíóú"
contador = 0
#Iteración de cada caracter del texto ingresado, convertirlo en minúsculas por si el texto contiene mayúsculas
# para despues comparar cada caracter del texto ingresado en la cadena estática y contabilizar las vocales
for caracter in txt:
    if caracter.lower() in vocales:
        contador +=1
#Mostrar el contador
print("La cantidad de vocales en el texto ingresado es: ",contador)

#Números de la Serie Fibonacci: 
# 10) Genera los primeros 10 números de la serie Fibonacci. 
#inicializando la lista con los valores 0,1
fibonacci = [0,1]
#Iteración paara recorrer los 8 primeros números naturales, para agregar a la lista fibonacci, recordar que 
#ya esta el 0 y 1
for i in range(0,8):
    fibonacci.append(fibonacci[-1]+fibonacci[-2])
print(fibonacci)

# Ordenamiento de Lista: 
# 11) Ordena una lista de números ingresados por el usuario de menor a mayor. 
#Inicializando la lista vacia
lista = []
print("Presione 'x' para salir")
#Iteración para preguntar al usuario e ingrese los números
while True:
    numero = input("Ingrese el número:\n")
    #Condicional para parar la iteración de preguntar al usuario
    if numero == "x":
        break
    #Agregar el número a la lista
    lista.append(int(numero))
    #Ordenar la lista
    lista.sort()
#Mostrar la lista ordenada
print("La lista ordenada es:\n",lista)

#Palíndromo: 
# 12) Verifica si una palabra ingresada por el usuario es un palíndromo. 
#Dato de entrada
palabra = input("Ingrese la palabra:\n")
#Quitar los espacios de la cadena
cadena = palabra.replace(" ","")
#Condicional para verificar si la cadena es palindroma
if cadena == cadena[::-1]:
    print("Es palíndomo!!!")
else:
    print("No es palíndromo!!!")

# Generador de Tablas de Multiplicar: 
# 13) Crea un programa que genere la tabla de multiplicar de un número ingresado por el usuario. 
#Ingreso de dato
numero = int(input("Ingrese un número:\n"))
#Iteración desde 1 hasta el número ingresado por el usuario
for i in range(1,numero+1):
    producto = str(numero) + " x "+ str(i) + " = "+str(numero * i)
    print(producto)

# Cálculo del Área de un Círculo: 
# 14) Pide el radio de un círculo al usuario y calcula su área. 
#Importar libreria math
import math
#Ingreso de dato
radio = int(input("Ingresa el radio del circulo:\n"))
#Operación para hallar el área
area = math.pi * radio*radio
#Mostrar resultado
print("El área del circulo es: "+str(area))

# Suma de Dígitos: 
# 15) Toma un número entero y calcula la suma de sus dígitos. 
#Ingreso de dato
cadena = input("Ingrese un número:\n")
#Inicializando la variable suma
suma = 0
#Iterar cada digito del número ingresado
for numero in cadena:
    suma += int(numero)
#Mostrar resultado
print("La suma de los digitos de '"+cadena+"' es: "+str(suma))
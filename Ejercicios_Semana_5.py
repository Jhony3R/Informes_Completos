# ---------------------------------------------------------------------------------------------------------
# 1. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números primos.
#Función para determinar los números primos
def numeros_primos(num, div = 2):
    if int(num) >=2:
        if div >= int(num):
            return True
        elif int(num) % div != 0 :
            return numeros_primos(num,div + 1)
        else:
            return False
    else:
        return False
#Función para agregar los números primos encontrados en los datos de entrada
def conjunto_numeros_primos(conjunto):
    conjunto_numeros_primos = set()
    for i in conjunto:
        if numeros_primos(i):
            conjunto_numeros_primos.add(i)
    return conjunto_numeros_primos
#Iteración para preguntar al usuario y que ingrese los números
print("PRESIONE X PARA SALIR")
conjunto_numeros = set()
while True:
    numeros = input("Ingrese número:\n")
    if numeros == "x":
        break
    conjunto_numeros.add(numeros)
#Mostrar los resultados   
print("El conjunto de los números ingresados es:",conjunto_numeros)
print("Los números primos en el conjunto ingresado es:",conjunto_numeros_primos(conjunto_numeros))

# ---------------------------------------------------------------------------------------------------------
# 2.  Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que 
# comienzan con una letra determinada.
def palabras_con_letra(words, letra):
    #Implementamos una iteración en el conjunton de palabras y buscar las palabras con la inicial indicada
    return {palabra for palabra in words if palabra.startswith(letra)}
#Conjunto de palabras
conj_palabras = {"manzana", "mesa", "banana", "limón", "mira", "kiwi"}
letra = "m"
#Invocar la función y mostrar el resultado
resultado = palabras_con_letra(conj_palabras, letra)
print(resultado)

# ---------------------------------------------------------------------------------------------------------
# 3.  Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que 
# son divisibles por un número determinado.
#Creación de un conjunto con datos y el otro vacio
conjunto_numeros = {1,2,3,4,5,6,7,8,9,10}
conjunto_numeros_divisibles = set()
#Función para determinar los números divisibles por un número determinado
def numeros_divisibles(conjunto_numeros,divisor):
    for numero in conjunto_numeros:
        if numero % int(divisor) == 0:
            conjunto_numeros_divisibles.add(numero)
    print("Los números divisibles por",divisor,"son:",sorted(conjunto_numeros_divisibles))
#Invocar a la función
numeros_divisibles(conjunto_numeros,2)

# ---------------------------------------------------------------------------------------------------------
# 4.  Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que 
# están en ambos conjuntos.
def interseccion(conjunto1, conjunto2):
    return conjunto1 & conjunto2
#Crear y asignar valores a cada conjunto
conjunto_a = {10, 2, 3, 4, 5}
conjunto_b = {3, 4, 5, 10, 7}
#Uso de la función intersección para obtener los elementos comunes
resultado = interseccion(conjunto_a, conjunto_b)
print("Intersección:", resultado)

# ---------------------------------------------------------------------------------------------------------
# 5. Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que 
# están en el primer conjunto pero no en el segundo.
#Crear y asignar valores a cada conjunto
conjunto_numeros_1 = {1,2,3,4,5,6,7,8,9,10}
conjunto_numeros_2 = {1,3,4,6,7,9}

def conjunto_diferencia(conjunto_numeros_1,conjunto_numeros_2):
    #Uso de la función difference para obtener los elementos que no se repiten en el segundo conjunto
    diferencia = conjunto_numeros_1.difference(conjunto_numeros_2)
    print(sorted(diferencia))

conjunto_diferencia(conjunto_numeros_1,conjunto_numeros_2)

# ---------------------------------------------------------------------------------------------------------
# 6.  Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que 
# están en el segundo conjunto pero no en el primero.
#Función que hace la diferencia del conjunto2 y conjunton1
def diferencia_de_conjuntos(conjunto1, conjunto2):
    diferencia = conjunto2 - conjunto1
    return diferencia
#Crear y asignar valores a cada conjunt
conjunto1 = {10, 2, 30, 4, 5}
conjunto2 = {33, 4, 5, 60, 7}
#Invocar la función y mostrar los resultados
resultado = diferencia_de_conjuntos(conjunto1, conjunto2)
print("Diferencia entre conjuntos :", resultado)

# ---------------------------------------------------------------------------------------------------------
# 7. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son 
# anagramas.
#Conjunto de palabras
conjunto_palabras = {"raza","zara","mora","roma","pedro","camino","ballena","llenaba","luis","jorge"}
#Función que determina las palabras que son anagramas
def anagramas(palabra_1,palabra_2):
    return sorted(palabra_1) == sorted(palabra_2)
#Función que recorre las palabras de un conjunto, invoca a la otra función de anagramas para ver si los agrega 
#a un conjunto de palabras anagramas
def conjunto_anagramas(conjunto_palabras):
    conjunto_palabras = list(conjunto_palabras)
    palabra_repetida = set()
    for i in range(len(conjunto_palabras)):
        for j in range(i + 1, len(conjunto_palabras)):
            if anagramas(conjunto_palabras[i],conjunto_palabras[j]):
                palabra_repetida.add(conjunto_palabras[i])
                palabra_repetida.add(conjunto_palabras[j])
    return palabra_repetida
#Mostrar resultados
print("Las palabras anagramas son:",conjunto_anagramas(conjunto_palabras))

# ---------------------------------------------------------------------------------------------------------
# 8.   Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son 
# palíndromos.
# Función auxiliar para verificar si una palabra es un palíndromo
def es_palindromo(palabra):
    return palabra == palabra[::-1]
#Función para filtrar las palabras que son palíndromas del conjunto dado
def palabras_palindromas(conjunto_palabras):
    return {palabra for palabra in conjunto_palabras if es_palindromo(palabra)}

conjunto_de_palabras = {"oso", "casa", "radar", "python", "reconocer"}
palindromos = palabras_palindromas(conjunto_de_palabras)

print("Palíndromos encontrados:", palindromos)

# ---------------------------------------------------------------------------------------------------------
# 9.  Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que 
# tienen una longitud determinada.
conjunto_palabras = {"Raza","Zara","Mora ","Roma","Pedro","Camino","Ballena ","Llenaba","Luis","Jorge"}
def tamaño_palabras(conjunto_palabras,tamaño):
    palabras_igual_tamaño = set()
    for palabra in conjunto_palabras:
        if len(palabra) == int(tamaño):
            palabras_igual_tamaño.add(palabra)
    return palabras_igual_tamaño

print(tamaño_palabras(conjunto_palabras,5))

# ---------------------------------------------------------------------------------------------------------
# 10. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que 
# contienen una letra determinada.
def palabras_letra(conjunto_palabras, letra):
    palabras_con_la_letra = set()
    #Recorrer el conjunto para buscar palabras que contienen la letra indicada
    for palabra in conjunto_palabras:
        if letra in palabra:
            palabras_con_la_letra.add(palabra)
    return palabras_con_la_letra
#Conjunto y muestra de los resultados
conjunto_palabras = {"manzana", "torre", "inversion", "facultad", "cancer"}
letra_a_buscar = "n"
resultado = palabras_letra(conjunto_palabras, letra_a_buscar)
print(f"Palabras que contienen la letra '{letra_a_buscar}': {resultado}")

# ---------------------------------------------------------------------------------------------------------
# 11.  Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que 
# están ordenados de menor a mayor. 

conjunto_numeros = {3,8,9,6,7,45,1,2}
def ordenar_números(conjunto_numeros):
    print(sorted(conjunto_numeros))

ordenar_números(conjunto_numeros)

# ---------------------------------------------------------------------------------------------------------
# 12. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que 
# están ordenados de mayor a menor.
def ordenar_de_mayor_a_menor(conjunto_numeros):
    lista_numeros = list(conjunto_numeros)
    #Ordenar lista
    lista_numeros.sort(reverse=True)
   #Conjunto ordenado
    conjunto_ordenado = set(lista_numeros)
    return conjunto_ordenado
#Conjunto, invocar función y mostrar resultados
conjunto_original = {5, 20, 8, 10, 7}
conjunto_ordenado = ordenar_de_mayor_a_menor(conjunto_original)
print("Conjunto ordenado de mayor a menor:", conjunto_ordenado)

# ---------------------------------------------------------------------------------------------------------
# 13.   Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que 
# están duplicados. 
#Lista de numeros
conjunto_numeros = [3,8,2,6,7,4,1,2,4,7]
def numeros_duplicados(conjunto_numeros):
    #Creación de conjuntos vacios
    numeros_existentes = set()
    numeros_duplicados = set()
    #Recorrer cada numero para verificar si son existentes y asignarlos a un conjunto
    for numero in conjunto_numeros:
        if numero in numeros_existentes:
            numeros_duplicados.add(numero)
        else:
            numeros_existentes.add(numero)
    return numeros_duplicados
#Mostrar resultado
print("Los números duplicados son:",numeros_duplicados(conjunto_numeros))

# ---------------------------------------------------------------------------------------------------------
# 14. . Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que no 
# están duplicados.
#Función que reciba un conjunto de números y retorna un conjunto con los numeros no duplicados
def numeros_no_duplicados(conjunto_numeros):
    lista_sin_duplicados = list(set(conjunto_numeros))
    conjunto_resultante = set(lista_sin_duplicados)
    return conjunto_resultante
#Conjunto de números
conjunto_numeros_ejemplo = {10, 2, 10, 2, 4, 5, 7, 3, 7,11,12,11,4,2}
#Invocar a la función
resultado = numeros_no_duplicados(conjunto_numeros_ejemplo)
#Mostrar resultados
print("Números no duplicados en el conjunto:", resultado)

# ---------------------------------------------------------------------------------------------------------
# 15. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que 
# son primos y están ordenados de menor a mayor.
#Función para verificar los números primos
def numeros_primos(num, div = 2):
    if int(num) >=2:
        if div >= int(num):
            return True
        elif int(num) % div != 0 :
            return numeros_primos(num,div + 1)
        else:
            return False
    else:
        return False
#Función que recibe un conjunto  de números 
def conjunto_numeros_primos(conjunto):
    conjunto_numeros_primos = set()
    for i in conjunto:
        if numeros_primos(i):
            conjunto_numeros_primos.add(i)
    return conjunto_numeros_primos
#Iteración para preguntar al usuario los números que va  a ingresar y agregarlos a un conjunto
print("PRESIONE X PARA SALIR")
conjunto_numeros = set()
while True:
    numeros = input("Ingrese número:\n")
    if numeros == "x":
        break
    conjunto_numeros.add(numeros)
#Mostrar los resultados
print("El conjunto de los números ingresados es:",sorted(conjunto_numeros))
print("Los números primos en el conjunto ingresado es:",sorted(conjunto_numeros_primos(conjunto_numeros)))

# ---------------------------------------------------------------------------------------------------------
# 16. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son 
# palíndromos y están ordenadas de menor a mayor.
#Función para verificar si la palabra es palíndroma
def es_palindromo(palabra):
    return palabra == palabra[::-1]
#Función que recibe un conjunto de palabras e invoca a otra función que verifica palabras palindromas para
#despues guardarlas y ordenarlas en un conjunto
def palindromos_ordenados(conjunto_palabras):
    palindromos = {palabra for palabra in conjunto_palabras if es_palindromo(palabra)}
    conjunto_ordenado = sorted(palindromos)
    return conjunto_ordenado
#Conjunto de palabras
conjunto_palabras_ejemplo = {"radar", "oso", "limon", "reconocer", "cívico"}
#Invocar la función y mostrar los resultados
resultado = palindromos_ordenados(conjunto_palabras_ejemplo)
print("Palíndromos ordenados de menor a mayor:", resultado)

# ---------------------------------------------------------------------------------------------------------
# 17. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que 
# tienen una longitud determinada y están ordenadas de menor a mayor.
#Conjunto de palabras
conjunto_palabras = {"Raza","Zara","Mora ","Roma","Pedro","Camino","Ballena ","Llenaba","Luis","Jorge"}
#Función que recibe como parametros de entrada un conjunto de palabras y el tamaño de cada palabra, la función retorna las palabras con el tamaño indicado
def tamaño_palabras(conjunto_palabras,tamaño):
    palabras_igual_tamaño = set()
    for palabra in conjunto_palabras:
        if len(palabra) == int(tamaño):
            palabras_igual_tamaño.add(palabra)
    return sorted(palabras_igual_tamaño)
#Mostrar resultados
print(tamaño_palabras(conjunto_palabras,4))

# ---------------------------------------------------------------------------------------------------------
# 18.   Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que 
# contienen una letra determinada y están ordenadas de mayor a menor.
#Función que recibe un conjunto de palabras y una letra determinada, retorna
# las palabras que coincidan con la letra determinada
def palabras_con_letra(words, letra):
    return sorted({palabra for palabra in words if palabra.startswith(letra)},reverse=True)
#Conjunto de palabras
conj_palabras = {"manzana", "mesa", "banana", "limón", "mira", "kiwi"}
letra = "m"
#Invocar la función y mostrar el resultado
resultado = palabras_con_letra(conj_palabras, letra)
print(resultado)

# ---------------------------------------------------------------------------------------------------------
# 19.  Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que 
# están ordenados de menor a mayor y que no están duplicados.
#Conjunto de números
conjunto_numeros = [8,83,8,2,6,7,4,1,2,4,7,23]
#Función que recibe un conjunto de números y devuelve un conjunto con los números que estan ordenados de menor
# a mayor
def numeros_duplicados(conjunto_numeros):
    numeros_existentes = set()
    numeros_duplicados = set()
    for numero in conjunto_numeros:
        
        if numero in numeros_existentes:
            numeros_duplicados.add(numero)
        else:
            numeros_existentes.add(numero)
    return sorted(numeros_duplicados)
#Mostrar resultados
print(numeros_duplicados(conjunto_numeros))

# ---------------------------------------------------------------------------------------------------------
# 20.   Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son 
# palíndromos, tienen una longitud determinada y están ordenadas de menor a mayor.
#Función que verifica si las palabras son palíndromos
def es_palindromo(palabra):
    # Función auxiliar para verificar si una palabra es un palíndromo
    return palabra == palabra[::-1]
#Función que recibe un conjunto de palabras y devuelve un conjunto de palabras que son palíndromos, tienen
# una longitud determinada y están ordenadas de menor a mayor
def palabras_palindromas(conjunto_palabras):
    # Filtra las palabras que son palíndromas del conjunto dado
    return sorted({palabra for palabra in conjunto_palabras if es_palindromo(palabra)})
#Conjunto, invocar a la función y mostrar los resultados
conjunto_de_palabras = {"oso", "casa", "radar", "python", "reconocer", "ana"}
palindromos = palabras_palindromas(conjunto_de_palabras)
print("Palíndromos encontrados:", palindromos)

# Recursividad:
# 1) Ejercicio 1: Escribe una función recursiva que imprima los números pares del 1 al 100.
def num_par(n):
    #Factor base
    if n == 0:
        return 0
    else:
        if n % 2 == 0:
            print(n) 
    #Factor recursivo
    num_par(n-1)
#Invocando a la función
num_par(100)

# 2) Ejercicio 2: Escribe una función recursiva que imprima la suma de los números del 1 al n.
def sum_num(n):
    #Factor base
    if n != 0:
        #Factor Recursivo
        return n + sum_num(n-1)
    else:
        return 0
#Invocar a la funcion
print(sum_num(5))

# 3) Ejercicio 3: Escribe una función recursiva que imprima la pirámide de números del 1 al n.
def piramide(n,f=1):
    cadena = ""
    #Factor base
    if f > n :
        return 0
    else:
        for i in range (0,f):
            cadena += str(f) + " "
        print(cadena)
        #Factor recursivo
    piramide(n,f+1)
#Invocar a la función
piramide(5)

# 4) Ejercicio 4: Escribe una función recursiva que imprima la pirámide de números invertidos del 1 al n.
def piramide_inversa(n):
    cadena = ""
    #Factor base
    if n != 0:
        for i in range (0,n):
            cadena += str(n) + " "
        print(cadena)
    else:
        return
    #Factor recursivo
    piramide_inversa(n-1)
#Invocar a la función
piramide_inversa(5)

# 5) Ejercicio 2: Escribe una función recursiva que imprima la tabla de multiplicar del n.
def producto(n,m=1):
    cadena = ""
    #Factor base
    if m > n:
        return 0
    else:
        cadena = str(n) + " x " + str(m) + " = " + str(n*m) + " "
        print(cadena)
    #Factor recursivo
    producto(n,m+1)
#Invocar a la función
producto(12)

# Arreglos y Matrices:
import numpy as np
# 6) Crea una matriz de números reales.
#Matriz
matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
#Mostrar matriz
print("La matriz de numeros reales es:\n",matriz)

# 7) Crea una matriz de números complejos.
#Matriz de números complejos
matriz_compleja = np.array([[1+1j,2,3],[4,5+5j,6],[7,8,9+9j]])
#Mostrar matriz
print("La matriz compleja es: ",matriz_compleja)

# 8) Crea una matriz de matrices.
#Creando matrices y asignando sus valores
matriz_1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
matriz_2 = np.array([[7,8,9],[10,11,12],[13,14,15]])
#Generando una matriz de matrices
matriz_de_matriz = np.array([matriz_1,matriz_2])
#Mostrar la nueva matriz
print("Un ejemplo de matriz de una matriz es: ",matriz_de_matriz)

# 9) Accede al elemento central de una matriz.
#Creando y asignando valores a la matriz
matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
#Obteniendo las dimensiones de las filas y columnas de la matriz
filas, columnas = matriz.shape
#Condicional para acceder al elemento central
if filas % 2 == 0 or columnas % 2 == 0:
    print("No se puede hallar el termino central")
else:
    fila_central = filas // 2
    columna_central = columnas // 2
    elemento_central = matriz[fila_central, columna_central]
    print("El elemento central de la matriz es: ", elemento_central)

# 10) Suma dos matrices de diferentes tamaños.
matriz1 = np.array([[1,2],[3,4],[5,6]])
matriz2 = np.array([[7,8,9],[10,11,12],[13,14,15]])

# Rellenar la matriz más pequeña con ceros
if matriz1.shape[0] < matriz2.shape[0]:
    matriz1 = np.pad(matriz1, ((0, matriz2.shape[0] - matriz1.shape[0]), (0, 0)), 'constant')
elif matriz1.shape[1] < matriz2.shape[1]:
    matriz1 = np.pad(matriz1, ((0, 0), (0, matriz2.shape[1] - matriz1.shape[1])), 'constant')

# Sumar las matrices
resultado = matriz1 + matriz2
# Mostrar el resultado
print("Matriz 1:")
print(matriz1)
print("\nMatriz 2:")
print(matriz2)
print("\nResultado de la suma:")
print(resultado)

# 11) Multiplica una matriz por un número.
#Creando la matriz y asignando valores
matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
#Multiplicando la matriz por un número
producto = matriz * 2
#Mostrar el resultado
print("El producto de una matriz por un número escalar es: \n",producto)

# 12) Calcula la media de los elementos de una matriz.
#Creando la matriz y asignando valores
matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
#La media de la matriz
media = np.mean(matriz)

# Ejercicio parte 01:
import numpy as np
# Ejercicio 1:
# Crea una matriz de números aleatorios de tamaño 100x100.
# Crear la matriz de números aleatorios
matriz_aleatoria = np.random.rand(100, 100)

# Mostrar la matriz aleatoria
print(matriz_aleatoria)

# Ejercicio 2:
# Calcula la media, la mediana y la desviación estándar de los elementos de una matriz.
#Creamos y asignamos valores a una matriz
matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
# Calcular la media de los elementos de la matriz
media = np.mean(matriz)
# Calcular la mediana de los elementos de la matriz
mediana = np.median(matriz)
# Calcular la desviación estándar de los elementos de la matriz
desviacion_estandar = np.std(matriz)
# Mostrar los resultados
print("Media:", media)
print("Mediana:", mediana)
print("Desviación estándar:", desviacion_estandar)

# Ejercicio 3:
# Escribe una función que encuentre el elemento máximo de una matriz.
#Creamos y asignamos valores a una matriz
matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
def encontrar_maximo(matriz):
    # Usamos la función np.max para encontrar el elemento máximo de la matriz
    maximo = np.max(matriz)
    return maximo
# Llamamos a la función para encontrar el elemento máximo
maximo = encontrar_maximo(matriz)
# Mostramos el resultado
print("El elemento máximo de la matriz es:", maximo)

# Ejercicio 4:
# Escribe una función que encuentre la submatriz de mayor suma de una matriz.
#Creamos y asignamos valores a una matriz
matriz = np.array([[1, 2, -3],
                   [4, 5, -6],
                   [7, -8, 9]])
def submatriz_mayor_suma(matriz):
    # Dimensiones de la matriz
    filas, columnas = matriz.shape
    
    # Inicializar variables para la submatriz de mayor suma encontrada hasta el momento
    max_suma = float('-inf')
    max_inicio_fila = 0
    max_fin_fila = 0
    max_inicio_col = 0
    max_fin_col = 0
    
    # Iterar sobre todas las submatrices posibles
    for inicio_fila in range(filas):
        for fin_fila in range(inicio_fila, filas):
            for inicio_col in range(columnas):
                for fin_col in range(inicio_col, columnas):
                    # Calcular la suma de la submatriz actual
                    suma_actual = np.sum(matriz[inicio_fila:fin_fila+1, inicio_col:fin_col+1])
                    
                    # Actualizar las variables si encontramos una suma mayor
                    if suma_actual > max_suma:
                        max_suma = suma_actual
                        max_inicio_fila = inicio_fila
                        max_fin_fila = fin_fila
                        max_inicio_col = inicio_col
                        max_fin_col = fin_col
    
    # Devolver la submatriz de mayor suma encontrada
    return matriz[max_inicio_fila:max_fin_fila+1, max_inicio_col:max_fin_col+1], max_suma

# Llamamos a la función para encontrar la submatriz de mayor suma
submatriz, suma = submatriz_mayor_suma(matriz)

# Mostramos el resultado
print("Submatriz de mayor suma:")
print(submatriz)
print("Suma de la submatriz de mayor suma:", suma)

# Ejercicio 5:
# Escribe una función que encuentre la matriz de covarianza de dos matrices.
matriz1 = np.array([[1,2],[3,4],[5,6]])
matriz2 = np.array([[7,8,9],[10,11,12],[13,14,15]])
def matriz_covarianza_entre_matrices(matriz1, matriz2):
    # Calcular la matriz de covarianza entre las dos matrices
    covarianza_entre_matrices = np.cov(matriz1, matriz2, rowvar=False)
    return covarianza_entre_matrices

# Llamamos a la función para encontrar la matriz de covarianza entre las dos matrices
covarianza_entre_matrices = matriz_covarianza_entre_matrices(matriz1, matriz2)

# Mostramos el resultado
print("Matriz de covarianza entre las dos matrices:")
print(covarianza_entre_matrices)



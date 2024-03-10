# # Ejercicio parte 01 – Listas Enlazadas Dobles:
# # Duplicar Nodos:
# # 1. Crea una lista con al menos 4 nodos, duplica cada nodo de la lista e imprime la lista original y la lista 
# # duplicada hacia adelante y hacia atrás.
# class Nodo:
#     def __init__(self, valor):
#         self.valor = valor
#         self.siguiente = None
#         self.anterior = None

# # Crear nodos
# nodo1 = Nodo(1)
# nodo2 = Nodo(2)
# nodo3 = Nodo(3)
# nodo4 = Nodo(4)

# # Crear lista
# lista_original = [nodo1, nodo2, nodo3, nodo4]

# # Duplicar cada nodo
# lista_duplicada = []
# for nodo in lista_original:
#     # Duplicar hacia adelante
#     nuevo_nodo_adelante = Nodo(nodo.valor)
#     nuevo_nodo_adelante.anterior = nodo
#     if nodo.siguiente:
#         nodo.siguiente.anterior = nuevo_nodo_adelante
#     nuevo_nodo_adelante.siguiente = nodo.siguiente
#     nodo.siguiente = nuevo_nodo_adelante

#     # Duplicar hacia atrás
#     nuevo_nodo_atras = Nodo(nodo.valor)
#     nuevo_nodo_atras.siguiente = nodo
#     if nodo.anterior:
#         nodo.anterior.siguiente = nuevo_nodo_atras
#     nuevo_nodo_atras.anterior = nodo.anterior
#     nodo.anterior = nuevo_nodo_atras

#     lista_duplicada.extend([nuevo_nodo_adelante, nuevo_nodo_atras])

# # Función para imprimir una lista de nodos
# def imprimir_lista(lista):
#     for nodo in lista:
#         print(f"Nodo {nodo.valor} -> ", end="")
#     print("None")

# # Imprimir listas originales y duplicadas
# print("Lista Original:")
# imprimir_lista(lista_original)

# print("\nLista Duplicada:")
# imprimir_lista(lista_duplicada)

# # Imprimir listas originales y duplicadas hacia atrás
# print("\nLista Original hacia atrás:")
# imprimir_lista(reversed(lista_original))

# print("\nLista Duplicada hacia atrás:")
# imprimir_lista(reversed(lista_duplicada))

# Contar Nodos Pares e Impares:
# 2. Crea una lista con al menos 9 nodos, cuenta cuántos nodos tienen un dato par y cuántos tienen un dato 
# impar e imprime la lista hacia adelante y hacia atrás.

# class NodoDoble:
#     def __init__(self, dato):
#         self.dato = dato
#         self.siguiente = None
#         self.anterior = None

# class ListaEnlazadaDoble:
#     def __init__(self):
#         self.inicio = None
#         self.fin = None

#     def insertar_al_principio(self, dato):
#         nuevo_nodo = NodoDoble(dato)
#         if not self.inicio:
#             self.inicio = self.fin = nuevo_nodo
#         else:
#             nuevo_nodo.siguiente = self.inicio
#             self.inicio.anterior = nuevo_nodo
#             self.inicio = nuevo_nodo

#     def insertar_al_final(self, dato):
#         nuevo_nodo = NodoDoble(dato)
#         if not self.fin:
#             self.inicio = self.fin = nuevo_nodo
#         else:
#             nuevo_nodo.anterior = self.fin
#             self.fin.siguiente = nuevo_nodo
#             self.fin = nuevo_nodo

#     def imprimir_adelante(self):
#         actual = self.inicio
#         while actual:
#             print(actual.dato, end=" <-> ")
#             actual = actual.siguiente
#         print("None")

#     def imprimir_atras(self):
#         actual = self.fin
#         while actual:
#             print(actual.dato, end=" <-> ")
#             actual = actual.anterior
#         print("None")

#     def contar_pares_impares(self):
#         actual = self.inicio
#         nodos_pares = 0
#         nodos_impares = 0

#         while actual:
#             if actual.dato % 2 == 0:
#                 nodos_pares += 1
#             else:
#                 nodos_impares += 1
#             actual = actual.siguiente

#         return nodos_pares, nodos_impares

# # Crear la lista con al menos 9 nodos
# lista_doble = ListaEnlazadaDoble()
# for i in range(1, 10):
#     lista_doble.insertar_al_final(i)

# # Imprimir la lista hacia adelante y hacia atrás
# print("Lista hacia adelante:")
# lista_doble.imprimir_adelante()

# print("\nLista hacia atrás:")
# lista_doble.imprimir_atras()

# # Contar nodos pares e impares
# nodos_pares, nodos_impares = lista_doble.contar_pares_impares()

# print("\nNodos Pares:", nodos_pares)
# print("Nodos Impares:", nodos_impares)

# Insertar Nodo en Posición Específica:
# 3. Crea una lista con al menos 5 nodos, inserta un nuevo nodo con el dato 15 en la posición 3 e imprime la 
# lista hacia adelante y hacia atrás.
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

# Función para imprimir una lista de nodos hacia adelante
def imprimir_lista_adelante(nodo):
    while nodo:
        print(nodo.valor, end=" -> ")
        nodo = nodo.siguiente
    print("None")

# Función para imprimir una lista de nodos hacia atrás
def imprimir_lista_atras(nodo):
    while nodo:
        print(nodo.valor, end=" -> ")
        nodo = nodo.anterior
    print("None")

# Crear nodos
nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)

# Construir lista
nodo1.siguiente = nodo2
nodo2.anterior = nodo1
nodo2.siguiente = nodo3
nodo3.anterior = nodo2
nodo3.siguiente = nodo4
nodo4.anterior = nodo3
nodo4.siguiente = nodo5
nodo5.anterior = nodo4

# Insertar nuevo nodo con dato 15 en la posición 3
nuevo_nodo = Nodo(15)
temp = nodo1
for _ in range(2):
    temp = temp.siguiente

nuevo_nodo.siguiente = temp.siguiente
temp.siguiente.anterior = nuevo_nodo
temp.siguiente = nuevo_nodo
nuevo_nodo.anterior = temp

# Imprimir lista hacia adelante
print("Lista hacia adelante:")
imprimir_lista_adelante(nodo1)

# Imprimir lista hacia atrás
print("\nLista hacia atrás:")
imprimir_lista_atras(nodo5)

# Eliminar Nodos Duplicados:
# 4. Crea una lista con nodos que contengan datos duplicados, elimina todos los nodos duplicados, dejando 
# solo una instancia de cada dato e imprime la lista hacia adelante y hacia atrás
# class NodoDoble:
#     def __init__(self, dato):
#         self.dato = dato
#         self.siguiente = None
#         self.anterior = None

# class ListaEnlazadaDoble:
#     def __init__(self):
#         self.inicio = None
#         self.fin = None

#     def insertar_al_final(self, dato):
#         nuevo_nodo = NodoDoble(dato)
#         if not self.fin:
#             self.inicio = self.fin = nuevo_nodo
#         else:
#             nuevo_nodo.anterior = self.fin
#             self.fin.siguiente = nuevo_nodo
#             self.fin = nuevo_nodo

#     def imprimir_adelante(self):
#         actual = self.inicio
#         while actual:
#             print(actual.dato, end=" <-> ")
#             actual = actual.siguiente
#         print("None")

#     def imprimir_atras(self):
#         actual = self.fin
#         while actual:
#             print(actual.dato, end=" <-> ")
#             actual = actual.anterior
#         print("None")

#     def eliminar_duplicados(self):
#         datos_vistos = set()
#         actual = self.inicio

#         while actual:
#             if actual.dato in datos_vistos:
#                 siguiente_nodo = actual.siguiente
#                 self.eliminar(actual)
#                 actual = siguiente_nodo
#             else:
#                 datos_vistos.add(actual.dato)
#                 actual = actual.siguiente

#     def eliminar(self, nodo):
#         if nodo.anterior:
#             nodo.anterior.siguiente = nodo.siguiente
#         else:
#             self.inicio = nodo.siguiente

#         if nodo.siguiente:
#             nodo.siguiente.anterior = nodo.anterior
#         else:
#             self.fin = nodo.anterior

# # Crear la lista con nodos duplicados
# lista_doble = ListaEnlazadaDoble()
# datos = [1, 2, 3, 2, 4, 5, 6, 4, 7, 10, 42, 15, 10]
# for dato in datos:
#     lista_doble.insertar_al_final(dato)

# # Imprimir la lista con duplicados
# print("Lista con duplicados:")
# lista_doble.imprimir_adelante()

# # Eliminar duplicados
# lista_doble.eliminar_duplicados()

# # Imprimir la lista después de eliminar duplicados
# print("\nLista sin duplicados:")
# lista_doble.imprimir_adelante()

# Invertir la Lista:
# 5. Crea una lista con al menos 6 nodos, invierte el orden de la lista (el último elemento se convierte en el 
# primero y viceversa) e imprime la lista hacia adelante y hacia atrás.
# class Nodo:
#     def __init__(self, dato):
#         self.dato = dato
#         self.siguiente = None

# # Función para imprimir la lista hacia adelante
# def imprimir_adelante(nodo):
#     while nodo:
#         print(nodo.dato, end=" ")
#         nodo = nodo.siguiente
#     print()

# # Función para imprimir la lista hacia atrás
# def imprimir_atras(nodo):
#     if nodo is None:
#         return
#     imprimir_atras(nodo.siguiente)
#     print(nodo.dato, end=" ")

# # Creamos una lista de nodos con al menos 6 nodos
# nodo6 = Nodo(1)
# nodo5 = Nodo(2)
# nodo4 = Nodo(3)
# nodo3 = Nodo(4)
# nodo2 = Nodo(5)
# nodo1 = Nodo(6)

# nodo1.siguiente = nodo2
# nodo2.siguiente = nodo3
# nodo3.siguiente = nodo4
# nodo4.siguiente = nodo5
# nodo5.siguiente = nodo6

# # Invertimos el orden de la lista
# nodo_actual = nodo1
# nodo_anterior = None

# while nodo_actual:
#     siguiente_nodo = nodo_actual.siguiente
#     nodo_actual.siguiente = nodo_anterior
#     nodo_anterior = nodo_actual
#     nodo_actual = siguiente_nodo

# # Imprimimos la lista hacia adelante
# print("Lista hacia adelante:")
# imprimir_adelante(nodo_anterior)

# # Imprimimos la lista hacia atrás
# print("Lista hacia atrás:")
# imprimir_atras(nodo_anterior)

# Invertir una cadena:
# 6. Utilizar una pila para invertir el orden de los caracteres de una cadena
# class Pila:
#     def __init__(self):
#         self.items = []

#     def apilar(self, item):
#         self.items.append(item)

#     def desapilar(self):
#         if not self.esta_vacia():
#             return self.items.pop()

#     def esta_vacia(self):
#         return len(self.items) == 0

# def invertir_cadena_con_pila(cadena):
#     pila = Pila()

#     # Apilar cada caracter en la pila
#     for caracter in cadena:
#         pila.apilar(caracter)

#     cadena_invertida = ""

#     # Desapilar para obtener la cadena invertida
#     while not pila.esta_vacia():
#         cadena_invertida += pila.desapilar()

#     return cadena_invertida

# # Ejemplo de uso
# cadena_original = "1,3,5,9,11,13,16,20,25,30 "
# cadena_invertida = invertir_cadena_con_pila(cadena_original)

# print("Cadena Original:", cadena_original)
# print("Cadena Invertida:", cadena_invertida)

# Convertir número decimal a binario:
# 7. Implementar un programa que convierta un número decimal a su representación en sistema binario 
# utilizando una pila.

# class Pila:
#     def __init__(self):
#         self.items = []

#     def esta_vacia(self):
#         return len(self.items) == 0

#     def apilar(self, item):
#         self.items.append(item)

#     def desapilar(self):
#         if not self.esta_vacia():
#             return self.items.pop()
#         else:
#             return None

# def decimal_a_binario(numero):
#     pila = Pila()

#     # Convertimos el número decimal a binario usando la técnica de división por 2
#     while numero > 0:
#         residuo = numero % 2
#         pila.apilar(residuo)
#         numero //= 2

#     # Construimos el número binario a partir de los elementos de la pila
#     binario = ""
#     while not pila.esta_vacia():
#         binario += str(pila.desapilar())

#     return binario if binario else "0"

# # Función principal para probar la conversión
# def main():
#     numero_decimal = float(input("Ingrese un número decimal: "))
#     numero_binario = decimal_a_binario(numero_decimal)
#     print("El número binario correspondiente es:", numero_binario)

# if __name__ == "__main__":
#     main()

# Evaluar expresión posfija:
# 8. Crear un programa que evalúe una expresión matemática en notación posfija utilizando una pila.
# class Pila:
#     def __init__(self):
#         self.items = []

#     def apilar(self, item):
#         self.items.append(item)

#     def desapilar(self):
#         if not self.esta_vacia():
#             return self.items.pop()

#     def esta_vacia(self):
#         return len(self.items) == 0

# def evaluar_expresion_posfija(expresion):
#     pila = Pila()

#     operadores = set(['+', '-', '*', '/'])

#     for elemento in expresion.split():
#         if elemento not in operadores:
#             # Si es un operando, apílalo
#             pila.apilar(float(elemento))
#         else:
#             # Si es un operador, realiza la operación
#             operando2 = pila.desapilar()
#             operando1 = pila.desapilar()

#             if elemento == '+':
#                 resultado = operando1 + operando2
#             elif elemento == '-':
#                 resultado = operando1 - operando2
#             elif elemento == '*':
#                 resultado = operando1 * operando2
#             elif elemento == '/':
#                 resultado = operando1 / operando2

#             # Apila el resultado de la operación
#             pila.apilar(resultado)

#     # Al final, el resultado estará en la cima de la pila
#     return pila.desapilar()

# # Ejemplo de uso
# expresion_posfija = "3 5 + 2 *"
# resultado = evaluar_expresion_posfija(expresion_posfija)

# print("Expresión posfija:", expresion_posfija)
# print("Resultado:", resultado)

# Validar operadores anidados:
# 9. Verificar si los operadores en una expresión matemática están correctamente anidados utilizando una 
# pila.
# class Pila:
#     def __init__(self):
#         self.items = []

#     def esta_vacia(self):
#         return len(self.items) == 0

#     def apilar(self, item):
#         self.items.append(item)

#     def desapilar(self):
#         if not self.esta_vacia():
#             return self.items.pop()
#         else:
#             return None

# def verificar_anidamiento(expresion):
#     pila = Pila()

#     for caracter in expresion:
#         if caracter == '(':
#             pila.apilar(caracter)
#         elif caracter == ')':
#             if pila.esta_vacia() or pila.desapilar() != '(':
#                 return False
    
#     return pila.esta_vacia()

# # Función principal para probar la verificación de anidamiento
# def main():
#     expresion_correcta = "(2 + 3) * (4 - 1)"
#     expresion_incorrecta = "(2 + 3) * (4 - 1"

#     resultado_correcto = verificar_anidamiento(expresion_correcta)
#     resultado_incorrecto = verificar_anidamiento(expresion_incorrecta)

#     print("Expresión correcta:", resultado_correcto)
#     print("Expresión incorrecta:", resultado_incorrecto)

# if __name__ == "__main__":
#     main()

# Ordenar una pila:
# 10. Ordenar los elementos de una pila de manera ascendente utilizando estructuras adicionales.
# class Pila:
#     def __init__(self):
#         self.items = []

#     def apilar(self, item):
#         self.items.append(item)

#     def desapilar(self):
#         if not self.esta_vacia():
#             return self.items.pop()

#     def esta_vacia(self):
#         return len(self.items) == 0

# def ordenar_pila(pila):
#     pila_ordenada = Pila()

#     while not pila.esta_vacia():
#         elemento_actual = pila.desapilar()

#         # Desapilar elementos mayores de la pila ordenada y apilarlos en la original
#         while not pila_ordenada.esta_vacia() and pila_ordenada.items[-1] > elemento_actual:
#             pila.apilar(pila_ordenada.desapilar())

#         # Apilar el elemento actual en la pila ordenada
#         pila_ordenada.apilar(elemento_actual)

#     return pila_ordenada

# # Ejemplo de uso
# pila_original = Pila()
# elementos = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 11, 20, 14, 50]
# for elemento in elementos:
#     pila_original.apilar(elemento)

# print("Pila original:", pila_original.items)

# pila_ordenada = ordenar_pila(pila_original)
# print("Pila ordenada:", pila_ordenada.items)

# Eliminar duplicados:
# 11. Eliminar los elementos duplicados de una pila.
# class Pila:
#     def __init__(self):
#         self.items = []

#     def esta_vacia(self):
#         return len(self.items) == 0

#     def apilar(self, item):
#         self.items.append(item)

#     def desapilar(self):
#         if not self.esta_vacia():
#             return self.items.pop()
#         else:
#             return None

# def eliminar_duplicados(pila):
#     pila_auxiliar = Pila()
#     elementos_unicos = set()

#     # Pasamos los elementos de la pila original a la pila auxiliar, eliminando duplicados
#     while not pila.esta_vacia():
#         elemento = pila.desapilar()
#         if elemento not in elementos_unicos:
#             pila_auxiliar.apilar(elemento)
#             elementos_unicos.add(elemento)

#     # Pasamos los elementos de la pila auxiliar de regreso a la pila original
#     while not pila_auxiliar.esta_vacia():
#         pila.apilar(pila_auxiliar.desapilar())

# # Función principal para probar la eliminación de duplicados
# def main():
#     pila = Pila()
#     # Llenar la pila con elementos, aquí puedes modificar según tus necesidades
#     elementos = [1, 2, 3, 3, 4, 5, 5, 6]
#     for elemento in elementos:
#         pila.apilar(elemento)

#     print("Pila original:", pila.items)
#     eliminar_duplicados(pila)
#     print("Pila sin duplicados:", pila.items)

# if __name__ == "__main__":
#     main()

# Implementar una calculadora sencilla:
# 12. Crear una calculadora que pueda realizar operaciones básicas (+, -, *, /) utilizando una pila para evaluar 
# expresiones.
# class Pila:
#     def __init__(self):
#         self.items = []

#     def apilar(self, item):
#         self.items.append(item)

#     def desapilar(self):
#         if not self.esta_vacia():
#             return self.items.pop()

#     def esta_vacia(self):
#         return len(self.items) == 0

# def infix_a_postfix(expresion):
#     pila_operadores = Pila()
#     resultado = []
#     precedencia = {'+': 1, '-': 1, '*': 2, '/': 2}

#     for caracter in expresion:
#         if caracter.isalnum():
#             resultado.append(caracter)
#         elif caracter == '(':
#             pila_operadores.apilar(caracter)
#         elif caracter == ')':
#             while pila_operadores.esta_vacia() is False and pila_operadores.items[-1] != '(':
#                 resultado.append(pila_operadores.desapilar())
#             pila_operadores.desapilar()  # Desapilar el paréntesis izquierdo
#         else:
#             while pila_operadores.esta_vacia() is False and precedencia.get(pila_operadores.items[-1], 0) >= precedencia.get(caracter, 0):
#                 resultado.append(pila_operadores.desapilar())
#             pila_operadores.apilar(caracter)

#     while pila_operadores.esta_vacia() is False:
#         resultado.append(pila_operadores.desapilar())

#     return ' '.join(resultado)

# def calcular(expresion):
#     pila = Pila()

#     for elemento in expresion.split():
#         if elemento.isdigit() or (elemento[0] == '-' and elemento[1:].isdigit()):
#             # Si es un número o un número negativo, apílalo
#             pila.apilar(float(elemento))
#         else:
#             # Si es un operador, realizar la operación
#             operando2 = pila.desapilar()
#             operando1 = pila.desapilar()

#             if elemento == '+':
#                 resultado = operando1 + operando2
#             elif elemento == '-':
#                 resultado = operando1 - operando2
#             elif elemento == '*':
#                 resultado = operando1 * operando2
#             elif elemento == '/':
#                 resultado = operando1 / operando2

#             # Apilar el resultado de la operación
#             pila.apilar(resultado)

#     # Al final, el resultado estará en la cima de la pila
#     return pila.desapilar()

# # Obtener la expresión de usuario
# expresion_usuario = input("Ingrese la operación: ")

# # Convertir a notación posfija
# expresion_posfija = infix_a_postfix(expresion_usuario)
# print("Notación Posfija:", expresion_posfija)

# # Calcular el resultado
# resultado = calcular(expresion_posfija)
# print("Resultado:", resultado)

# Comprobar palíndromos:
# 13. Utilizar una pila para comprobar si una palabra o frase es un palíndromo.
# class Pila:
#     def __init__(self):
#         self.items = []

#     def esta_vacia(self):
#         return len(self.items) == 0

#     def apilar(self, item):
#         self.items.append(item)

#     def desapilar(self):
#         if not self.esta_vacia():
#             return self.items.pop()
#         else:
#             return None

# def es_palindromo(palabra):
#     pila = Pila()

#     # Eliminamos espacios en blanco y convertimos la palabra a minúsculas
#     palabra = palabra.replace(" ", "").lower()

#     # Apilamos los caracteres de la palabra
#     for caracter in palabra:
#         pila.apilar(caracter)

#     # Construimos la palabra invertida desapilando los caracteres de la pila
#     palabra_invertida = ""
#     while not pila.esta_vacia():
#         palabra_invertida += pila.desapilar()

#     # Comparamos la palabra original con la palabra invertida
#     return palabra == palabra_invertida

# # Función principal para probar si una palabra es un palíndromo
# def main():
#     palabra1 = "reconocer"
#     palabra2 = "Anita lava la tina"
#     palabra3 = "Esto es otra expresión"

#     resultado1 = es_palindromo(palabra1)
#     resultado2 = es_palindromo(palabra2)
#     resultado3 = es_palindromo(palabra3)

#     print("¿", palabra1, "es un palíndromo?", resultado1)
#     print("¿", palabra2, "es un palíndromo?", resultado2)
#     print("¿", palabra3, "es un palíndromo?", resultado3)

# if __name__ == "__main__":
#     main()

# Simular el proceso de deshacer (undo):
# 14. Implementar un sistema simple de "deshacer" utilizando dos pilas, una para las acciones y otra para los 
# deshaceres.
# class UndoSystem:
#     def __init__(self):
#         self.acciones = []  # Pila para almacenar las acciones
#         self.deshacer = []  # Pila para almacenar las acciones para deshacer

#     def hacer(self, accion):
#         print(f"Haciendo: {accion}")
#         self.acciones.append(accion)
#         self.deshacer = []  # Limpiar la pila de deshacer al hacer una nueva acción

#     def deshacer_accion(self):
#         if not self.acciones:
#             print("No hay acciones para deshacer.")
#             return

#         accion_deshacer = self.acciones.pop()
#         print(f"Deshaciendo: {accion_deshacer}")
#         self.deshacer.append(accion_deshacer)

#     def rehacer_accion(self):
#         if not self.deshacer:
#             print("No hay acciones para rehacer.")
#             return

#         accion_rehacer = self.deshacer.pop()
#         print(f'Rehaciendo: {accion_rehacer}')
#         self.acciones.append(accion_rehacer)

# # Ejemplo de uso
# sistema_undo = UndoSystem()

# while True:
#     print("\nMenú:")
#     print("1. Hacer")
#     print("2. Deshacer")
#     print("3. Rehacer")
#     print("4. Salir")

#     opcion = input("Seleccione una opción: ")

#     if opcion == "1":
#         accion = input("Ingrese la acción a realizar: ")
#         sistema_undo.hacer(accion)
#     elif opcion == "2":
#         sistema_undo.deshacer_accion()
#     elif opcion == "3":
#         sistema_undo.rehacer_accion()
#     elif opcion == "4":
#         print("Saliendo del programa.")
#         break
#     else:
#         print("Opción no válida. Intente nuevamente.")

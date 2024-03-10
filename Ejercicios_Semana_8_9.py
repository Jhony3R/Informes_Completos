#Ejercicio parte 01:
# 1.Validar la edad de un usuario.
def validar_edad_usuario(edad):
    assert len(str(edad)) >=1, 'Tienes que ingresar tu edad'
    assert isinstance(edad,int), 'Tu edad debe de ser un número'
    assert edad>=0, 'Tu edad no tiene que ser negativo'
    assert edad<=120, 'Tu edad no debe ser mayor a 120'

# Ingresamos la edad
edad = 35

try:
    validar_edad_usuario(edad)
    print("¡La edad ingresada es correcta!") 
except AssertionError as error:
    print('Error:',error)
# 2. Verificar el tipo de dato de una variable.
x = 5
assert isinstance(x, int), "x debe ser un entero"

y = "Hola Mundo"
assert isinstance(y, str), "y debe ser una cadena de texto"

z = [1, 2, 3]
assert isinstance(z, list), "z debe ser una lista"

# 3.Validar el rango de una calificación.
def validar_rango_calificacion(nota):
    assert len(str(nota)) >=1, 'Tienes que ingresar la calificación'
    assert isinstance(nota,int), 'La calificación debe de ser un número'
    assert nota>=0, 'La calificación no debe ser negativa'
    assert nota<=20, 'La calificación no debe ser mayor a 20'

# Ingresamos la calificación
nota = 35

try:
    validar_rango_calificacion(nota)
    print("¡La calificación ingresada es correcta!") 
except AssertionError as error:
    print('Error:',error)

# 4. Asegurar que una lista no esté vacía.
def asegurar_lista_no_vacia(lista):
    assert len(lista) > 0, 'La lista no debe estar vacía'

mi_lista = [1, 2, 3]
try:
    asegurar_lista_no_vacia(mi_lista)
    print('La lista no está vacía, puedes continuar.')
except AssertionError as e:
    print(f'Error: {e}')

# 5. Validar la igualdad de dos objetos
def validar_igualdad_objetos(objeto1,objeto2):
    assert objeto1==objeto2, 'Los objetos tienen que ser iguales'

# Ingresamos los objetos
objeto1 = 35
objeto2 = 35

try:
    validar_igualdad_objetos(objeto1,objeto2)
    print("¡Los objetos son iguales!") 
except AssertionError as error:
    print('Error:',error)
# 6. Asegurar que un ciclo while se ejecuta al menos una vez.
def ciclo_while():
    while True:
        respuesta = input('¿Quieres continuar? (Sí/No): ').lower()
        
        if respuesta == 'no':
            break  # Salir del bucle si la respuesta es 'no'
try:
    ciclo_while()
    print('El ciclo se ejecutó al menos una vez.')
except KeyboardInterrupt:
    print('\nSaliendo del programa.')

# 7. Asegurar que una función retorna un valor específico.
def suma_numeros(num1, num2):
    resultado = num1 + num2
    assert resultado > 0, "El resultado debe ser mayor que cero"
    return resultado

try:
    resultado = suma_numeros(2, 3)
    print("La suma es:", resultado)
except AssertionError as error:
    print("Error:", error)
#8. Validar el estado de una variable después de una operación.
def realizar_operacion_y_validar(variable):
  
    resultado = realizar_operacion(variable)
    assert alguna_condicion(resultado), 'La variable no tiene el estado esperado después de la operación'

def realizar_operacion(variable):
    return variable * 2

def alguna_condicion(resultado):
    return resultado > 0

mi_variable = 6
try:
    realizar_operacion_y_validar(mi_variable)
    print('La variable tiene el estado esperado después de la operación.')
except AssertionError as e:
    print(f'Error: {e}')
    
# 9. Asegurar que un módulo se ha importado correctamente.
try:
    import numpy
    assert numpy is not None, "Error al importar el módulo numpy"
    print("El módulo numpy se ha importado correctamente.")
except AssertionError and ModuleNotFoundError as error:
    print("Error:", error)

#10. Desarrollar el código de buscar nodo en la lista enlazada simple.
#Suma de Nodos
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_nodo(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def buscar_nodo(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    def suma_nodos(self):
        suma = 0
        actual = self.cabeza
        while actual:
            suma += actual.valor
            actual = actual.siguiente
        return suma

lista = ListaEnlazada()

# Agregar nodos a la lista
lista.agregar_nodo(2)
lista.agregar_nodo(5)
lista.agregar_nodo(8)
lista.agregar_nodo(10)

# Buscar un nodo en la lista
valor_a_buscar = 5
if lista.buscar_nodo(valor_a_buscar):
    print(f"El valor {valor_a_buscar} está en la lista.")
else:
    print(f"El valor {valor_a_buscar} no está en la lista.")

# Calcular la suma de los nodos
suma_total = lista.suma_nodos()
print(f"La suma de los nodos en la lista es: {suma_total}")

# 11. Implementa una función que sume todos los nodos de una lista enlazada simple.
#Clase Nodo
class Nodo:
    #Función para inicializar el dato
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None
#Clase enlazada simple
class ListaEnlazadaSimple:
    def __init__(self):
        self.inicio = None
    #Función que inserta valor en la lista indicada
    def insertar_valor(self,dato):
        nuevo_nodo = Nodo(dato)
        if not self.inicio:
            self.inicio = nuevo_nodo
            return
        actual = self.inicio
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo
    #Función que retorna la suma de los nodos
    def suma_nodos(self):
        suma = 0
        actual = self.inicio
        while actual:
            suma += actual.dato
            actual = actual.siguiente
        return suma

#Ejemplo
lista = ListaEnlazadaSimple()
lista.insertar_valor(1)
lista.insertar_valor(2)
lista.insertar_valor(3)
lista.insertar_valor(4)
#Mostrar resultados
print('La suma de todos los nodos de la lista enlazada simple es: ',lista.suma_nodos())

#12 Crea una función que devuelva la longitud de una lista enlazada simple.
#Concatenar Listas
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

def longitud_lista_enlazada(cabeza):
    longitud = 0
    actual = cabeza
    while actual:
        longitud += 1
        actual = actual.siguiente
    return longitud

def concatenar_listas_enlazadas(lista1, lista2):
    if not lista1:
        return lista2
    actual = lista1
    while actual.siguiente:
        actual = actual.siguiente
    actual.siguiente = lista2
    return lista1

# Ejemplo de uso
nodo1 = Nodo(2)
nodo2 = Nodo(5)
nodo3 = Nodo(8)

# Enlazar los nodos en la primera lista
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3

# Calcular la longitud de la primera lista
longitud = longitud_lista_enlazada(nodo1)
print(f"La longitud de la lista es: {longitud}")

# Crear una segunda lista enlazada
nodo4 = Nodo(10)
nodo5 = Nodo(15)

# Enlazar los nodos en la segunda lista
nodo4.siguiente = nodo5

# Concatenar las dos listas enlazadas
nueva_cabeza = concatenar_listas_enlazadas(nodo1, nodo4)
# Calcular la longitud de la lista concatenada
longitud_concatenada = longitud_lista_enlazada(nueva_cabeza)
print(f"La longitud de la lista concatenada es: {longitud_concatenada}")

# 13. Implementa una función que concatene dos listas enlazadas simples.
#Clase Nodo
class Nodo:
    #Función que inicializa el dato
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None
#Clase lista enlazada simple
class ListaEnlazadaSimple:
    def __init__(self):
        self.inicio = None
    #Función que inserta valor
    def insertar_valor(self,dato):
        nuevo_nodo = Nodo(dato)
        if not self.inicio:
            self.inicio = nuevo_nodo
            return
        actual = self.inicio
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo
    #Función para concatenar los datos
    def concatenar_datos(self,otra_lista):
        if not self.inicio:
            self.inicio = otra_lista.inicio
        else:
            actual = self.inicio
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = otra_lista.inicio
    #Función para mostrar el resultado
    def imprimir_lista(self):
        actual = self.inicio
        while actual:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()    
#Ejemplo
lista1 = ListaEnlazadaSimple()
lista1.insertar_valor(1)
lista1.insertar_valor(2)
lista1.insertar_valor(3)
lista1.insertar_valor(4)
print("Lista 1:", end=" ")
lista1.imprimir_lista()

lista2 = ListaEnlazadaSimple()
lista2.insertar_valor(5)
lista2.insertar_valor(6)
lista2.insertar_valor(7)
lista2.insertar_valor(8)
print("Lista 2:", end=" ")
lista2.imprimir_lista()

lista1.concatenar_datos(lista2)
print("Después de concatenar:")
lista1.imprimir_lista()

# 14. Crea una función que elimine los nodos duplicados de una lista enlazada simple.
#Invertir Lista
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

def eliminar_nodos_duplicados(cabeza):
    nodos_vistos = set()
    actual = cabeza
    previo = None

    while actual:
        if actual.valor in nodos_vistos:
            # Eliminar el nodo duplicado
            previo.siguiente = actual.siguiente
        else:
            # Agregar el valor actual al conjunto de nodos vistos
            nodos_vistos.add(actual.valor)
            # Mover al siguiente nodo
            previo = actual
        actual = actual.siguiente

def invertir_lista(cabeza):
    actual = cabeza
    previo = None

    while actual:
        siguiente = actual.siguiente
        actual.siguiente = previo
        previo = actual
        actual = siguiente

    return previo  # La nueva cabeza es el último nodo original

# Función para imprimir la lista enlazada
def imprimir_lista_enlazada(cabeza):
    actual = cabeza
    while actual:
        print(actual.valor, end=" -> ")
        actual = actual.siguiente
    print("None")

# Ejemplo de uso
nodo1 = Nodo(2)
nodo2 = Nodo(5)
nodo3 = Nodo(8)
nodo4 = Nodo(5)
nodo5 = Nodo(10)

# Enlazar los nodos en la lista original
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4
nodo4.siguiente = nodo5

print("Lista original:")
imprimir_lista_enlazada(nodo1)

# Eliminar nodos duplicados
eliminar_nodos_duplicados(nodo1)
print("\nLista sin nodos duplicados:")
imprimir_lista_enlazada(nodo1)

# Invertir la lista
nueva_cabeza = invertir_lista(nodo1)
print("\nLista invertida:")
imprimir_lista_enlazada(nueva_cabeza)

# 15. Implementa una función que invierta el orden de una lista enlazada simple.
#Clase Nodo
class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None
#Clase Lista enlazada simple
class ListaEnlazadaSimple:
    def __init__(self):
        self.inicio = None
    #Función para insertar valor en el nodo indicado
    def insertar_valor(self,dato):
        nuevo_nodo = Nodo(dato)
        if not self.inicio:
            self.inicio = nuevo_nodo
            return
        actual = self.inicio
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo
    #Función para invertir los datos
    def invertir_datos(self):
        anterior = None
        actual = self.inicio
        siguiente = None
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        self.inicio = anterior
    #Función para mostrar los resultados
    def imprimir_lista(self):
        actual = self.inicio
        while actual:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()    

#Ejemplo
lista = ListaEnlazadaSimple()
lista.insertar_valor(1)
lista.insertar_valor(2)
lista.insertar_valor(3)
lista.insertar_valor(4)

print("Lista Original:")
lista.imprimir_lista()
lista.invertir_datos()

print("Lista Invertida:")
lista.imprimir_lista()
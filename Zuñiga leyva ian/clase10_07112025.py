# Métodos de utilidad
lista_frutas = ["manzana", "banana", "cereza", "durazno", "mango"]
print(lista_frutas)

lista_frutas.append("kiwi") # Agrega un elemento al final de la lista
print(lista_frutas)

lista_frutas.pop() # Elimina el último elemento de la lista
print(lista_frutas)

lista_frutas.pop(2) # Elimina el elemento en la posicion 2 (tercer elemento)
print(lista_frutas)

lista_frutas.remove("banana") # Elimina el elemento con el valor "banana"
print(lista_frutas)

lista_frutas.insert(2, "uva") # Inserta "uva" en la posición 2
print(lista_frutas)

lista_frutas.clear() # Elimina todos los elementos de la lista
print(lista_frutas)

lista_frutas = [] # Reiniciamos la lista para los siguientes ejercicios
print(lista_frutas)

lista_frutas = ["manzana", "banana", "cereza", "durazno", "naranja"]

lista_frutas.index("cereza") # Devuelve el índice del elemento "cereza"
print(lista_frutas.index("cereza"))

lista_frutas.count("banana") # Cuenta cuántas veces aparece "banana" en la lista
print(lista_frutas.count("banana"))

lista_frutas.sort() # Ordena la lista en orden ascendente
print(lista_frutas)

lista_frutas.reverse() # Invierte el orden de los elementos en la lista
print(lista_frutas)

length = len(lista_frutas) # Devuelve la cantidad de elementos en la lista
print(len(lista_frutas))

lista = [5, 2, 9, 1, 5, 6]
print(sum(lista)) # Suma todos los elementos de la lista

# Ejercicio 1: Pide 5 numeros, guardalos en una lista, muestra el promedio y el mayor de los numeros
lista_numeros = [] #Declaramos una lista vacia para guardar los numeros

#Llenar la lista por medio de un for
for i in range(5):
    numero = float(input("Ingresa un número: "))
    lista_numeros.append(numero) #Agregamos el numero ingresado por consola a la lista

promerio = sum(lista_numeros) / len(lista_numeros) #Calculamos el promedio
num_mayor = max(lista_numeros) #Obtenemos el numero mayor con la funcion max() y lo guardamos en una variable
print(f"El promedio de los números ingresados es: {promerio}. y el número mayor es: {num_mayor}.")

# Ejercicio 2: Pide numeros hasta que el usuario escriba 0; guardalos en una lista y muestra la lista ordenada ascendentemente
lista_numeros = [] #Declaramos una lista vacia para guardar numeros
while True:
    numero = float(input("Ingresa un numero (Ingresa 0 para terminar): "))
    if numero == 0:
        break #salimos del ciclo si el usuario ingresa 0
    lista_numeros.append(numero) #Agregamos el numero ingresado por consola a la lista

    lista_numeros.sort() #Ordenamos la lista en orden acendente
    print("Lista ordenada:", lista_numeros)
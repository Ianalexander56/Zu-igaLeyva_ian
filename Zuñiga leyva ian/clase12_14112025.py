#Funciones en Python

#Definicion

def saludar():
    print("¡Hola, bienvenido a la clase de Python!")

#Llamada a la funcion
saludar()
saludar()
saludar()

#Funcion con parametros
def saludar_personal(nombre, apellido, edad):
    print(F"¡Hola {nombre} {apellido}, tienes {edad} años!")

#Llamada a la funcion con argumentos
saludar_personal("Mario", "Segovia", 29)
saludar_personal("Jorge", "Ramirez", 39)
saludar_personal("Jorge", "Zuñiga", 29) 

#Funcion con valor de retorno
def sumar(a, b):
    return a + b

print(sumar (3 + 5))
resultado = sumar(10,20)
print("El resultado de la suma es:", resultado)

#Sistemas de gestion de Estudiantes
def mostrar_menu():
    print("Sistemas de Gestion de Estudiantes")
    print("1. Agregar estudiante")
    print("2. Mostrar lista completa de estudiantes")
    print("3. Buscar estudiante por nombre")
    print("4. Eliminar estudiante")
    print("5. Salir")

#Funcion para agregar un estudiante
def agregar_estudiante(lista_estudiante):
    nombre = input("Ingrese el nombre del estudiantes")
    apellido = input("Ingrese el apellido del estudiante")
    promedio = input("Ingrese")   
    



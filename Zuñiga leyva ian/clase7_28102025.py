# Ejercicio 3: Haz un programa en Python que pida un numero entero y muestre cuantos numeros pares hay desde 1 hasta es numeros hay desde 1 hasta ese numero (incluyendo si es par)

conteo_pares = 0
#solicitar al usuario que ingrese un numero entero
numero = int(input("ingrese un numero entero: "))

for i in range(1, numero + 1):
    if i % 2 == 0:
        conteo_pares += 1
print(i)

print(f"Hay {conteo_pares} numeros pares desde 1 hasta {numero}. ")

#Ejercicio 4: Haz un programa en Python que pida un numero y calcule el factorial de ese numero
numero = int(input("ingrese un numero para calcular su factorial: "))
factorial = 1
for i in range(1, numero + 1):
    factorial *= i
    print(f"El factorial de {numero} es {factorial}. ")
    
#Bucle While
#while condicion:
#bloque de codigo

#Ejercicio 1: Haz un programa que pida al usuario ingresar un contraseña hasta que ingrese la contraseña correcta y que tenga maximo 5 intentos

#Definir contraseña correcta
contraseña_correcta = "Credinalga"
intentos = 0
max_intentos = 5
contraseña = input("ingrese la contraseña: ")

while (intentos < max_intentos) and (contraseña != contraseña_correcta):
    print("contraseña incorrecta. Intente de nuevo. ")
    intentos += 1
    contraseña = input("ingrese la contraseña: ")

if intentos == max_intentos:
    print("has excedido el numero maximo de intentos. Acceso denegado. ")
else:
    print(f"Contraseña correctas. Acceso concedido. Intentos realizados {intentos}. ")

#Ejercicio 2: Haz un programa que pida el usuario ingresar numeros positivos y que se detenga hasta que ingrese un numero negativo

numero = float(input("ingrese un numero positivo (o un numero negativo para salir): "))

while numero >= 0:
    numero = float(input("Ingrese un numero positivo (o un numero negativo para salir): "))

print("numero negativo ingresado. Programa terminado. ")

#Ejercicio 3: Haz un programa que sume todos lo numeros que ingrese el usuario hasta que ingrese un 0

suma = 0
numero = float(input("Ingrese un numero para sumar (o 0 para salir): "))

while numero != 0:
    suma += numero
    numero = float(input("Ingresa un numero para sumar (o 0 para salir): "))

print(f"la suma total de los numeros ingresados es: {suma}. ")

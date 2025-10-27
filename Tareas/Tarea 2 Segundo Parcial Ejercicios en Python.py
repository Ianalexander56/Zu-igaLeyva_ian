#1 Haz un programa en Python que pida tres calificaciones y calcule su promedio con dos decimales
print("ejercicio 1")

calificacion1 = float(input("ingresa la primera calificacion "))
calificacion2 = float(input("ingresa la segunda calificacion "))
calificacion3 = float(input("ingrese la tercera calificacion "))
promedio = (calificacion1 + calificacion2 + calificacion3) /3

round = (promedio, 2)

print(f"el promedio es, {promedio}")

#2 Haz un programa en Python que calcule el área de un círculo a partir de su radio
print("ejercicio 2")

import math

radio = float(input("ingrese el radio de tu circulo "))

potencia = math.pow (radio, 2)

area = (potencia * 3.1416)

print(f"el area del circulo es, {area}")

#3 Haz un programa en Python que calcule el perímetro de una circunferencia con base en su radio
print("ejercicio 3")

radio = float(input("ingresa el radio de tu circunferencia: "))

perimetro = ((radio * 2) * 3.1416)

print(F"el perimetro de tu circunferencia es: {perimetro}")

#4 Haz un programa en Python que convierta una cantidad de minutos a horas
print("ejercicio 4")

minutos = int(input("ingrese los minutos: "))

horas = (minutos / 60)

print(f"las horas totales son: {horas}")

#5 Haz un programa en Python que pida un precio y muestre el total con IVA del 16%
print("ejercicio 5")

precio = float(input("ingrese el precio: "))

iva = (precio * .16)
precioiva = (precio + iva)

print(f"el precio con iva es: {precioiva}")

#6 Haz un programa en Python que pida tres números y muestre si se cumple la expresión A < B < C (solo mostrando el resultado lógico) 
print("ejercicio 6")

num1 = float(input("ingrese el primer numero: "))
num2 = float(input("ingrese el segundo numero: "))
num3 = float(input("ingrese el tercer nunero: "))

resultado = num1 < num2 < num3

print(f"¿se cumple la expresion A < B < C? {resultado}")

#7 Haz un programa en Python que pida un número y muestre si está entre 10 y 20 (solo mostrando True o False)
print("ejercicio 7")

num = float(input("ingrese un numero: "))

numero = num>=10 and num<=20 

print(F"¿el numero esta entre 10 y 20? {numero}")

#8 Haz un programa en Python que pida tres números y muestre si los tres son iguales (solo mostrando True o False)
print("ejercicio 8")

num1 = float(input("ingrese el primer numero: "))
num2 = float(input("ingrese el segundo numero: "))
num3 = float(input("ingreese el tercer numero: "))

resultado = num1 == num2 == num3

print(f"¿los tres numero son iguales? {resultado}")

#9 Haz un programa en Python que pida tres números y muestre si los tres son iguales (solo mostrando True o False)
print("ejercicio 9")

num1 = float(input("ingrese el primer numero: "))
num2 = float(input("ingrese el segundo numero: "))
num3 = float(input("ingrese el tercer numero: "))

resultado = num1 == num2 == num3

print(f"¿los tres numero son iguales? {resultado}")

#10  Haz un programa en Python que pida el radio y la altura de un cilindro y muestre su volumen
print("ejercicio 10")

radio = float(input("ingresa el radio del cilindro: "))
altura = float(input("ingrese la altura del cilindro: "))

radiocuadrado = math.pow (radio, 2)
areabase = (radiocuadrado * 3.1416)
volumen = (areabase * altura)

print(f"el volumen del cilindro es: {volumen}")



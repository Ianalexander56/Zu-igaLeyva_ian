#Programa que pida un numero entero positivo y muestre su raiz cuadrada, raiz cubica
#potencia al cuadrado y potencia al cubo

import math

numero = int(input("ingrese un numero entero positivo: "))

RaizCuadrada = math.sqrt(numero)
RaizCubica = numero ** (1/3)
potenciacuadrado = pow(numero, 2)
potenciacubica = pow(numero, 3)

print(f"la raiz cuadrada de {numero} es: {RaizCuadrada}.")
print(f"la raiz cubica de {numero} es: {RaizCubica}.")
print(f"la potencia al cuadrado de {numero} es: {potenciacuadrado}.")
print(f"la potencia al cubo de {numero} es: {potenciacubica}.")

#Haz un programa que pida numeros enteros y muestre si se cumple la expresion:
# El primer numero es mayor que el segundo y el segundo menor que el tercero. Esto sin utilizar condiciones, solo operadores logicos

num1 = int(input("Ingrese el primer numero entero: "))
num2 = int(input("Ingrese el segundo numero entero: "))
num3 = int(input("Ingrese el tercer numero entero: "))
 

#1 Haz un programa en Python que pida un número, posteriormente muestra todos los números desde 1 hasta el número ingresando. Imprime en consola un coteo de números pares y de números impares.

# numero = int(input("ingrese un numero: "))

# pares = 0
# impares = 0

# for i in range(1, numero + 1):
#     if i % 2 == 0:
#         pares += 1
#     else:
#         impares += 1
        
# print(f"hay {pares} numeros pares y {impares} numeros impares")

# #2 Haz un programa que pida al usuario ingresar un nombre y una edad, verifica si la persona ingresada tiene la edad suficiente para votar (Tomando en cuenta que se puede votar a partir de los 18 años), si puede votar imprime un mensaje indicando que se puede votar, en caso de que no se pueda, imprime un mensaje indicando que no se puede votar y los años que le faltan para llegar poder votar.

# nombre = input("ingrese su nombre: ")
# edad = int(input("ingrese su edad: "))

# if edad >=18:
#     print(f"{nombre} usted tiene {edad} usted puede votar")
# else:
#     años_faltantes = 18 - edad
#     print(f"{nombre} usted tiene {edad} años, lamentablemente no puede votar, le faltan {años_faltantes}")

# #3 Haz un programa en Python que pida al usuario ingresar un número, y muestre su tabla de multiplicar del 1 al 20, pero solo para los múltiplos pares (Es decir, numero x 2, número x 4, número x 6, etc).

# numero = int(input("ingrese un numero si eres tan amable: "))
# print(f"Tabla de multiplicar de {numero} (numeros pares)")

# for i in range(2, 21, 2):
#     resultado = numero * i
#     print(f"{numero} * {i} = {resultado}")

# #4 Haz un programa que pida 5 números (Técnicamente podríamos almacenarlos en un arreglo, pero no hemos llegado ahí, así que NO LO HAGAS ASÍ, debes pedir los números y almacenarlos en variables diferentes), de los 5 números ingresados, muestra cuántos fueron mayores que 10.

# num1 = float(input("ingrese el primer numero: "))
# num2 = float(input("ingrese el segundo numero: "))
# num3 = float(input("ingrese el tercer numero: "))
# num4 = float(input("ingrese el cuarto numero: "))
# num5 = float(input("ingrese el quinto numero: "))

# conteo_mayores_10 = 0
# if num1 > 10:
#     conteo_mayores_10 += 1
# if num2 > 10:
#     conteo_mayores_10 += 1
# if num3 > 10:
#     conteo_mayores_10 += 1
# if num4 > 10:
#     conteo_mayores_10 += 1
# if num5 > 10:
#     conteo_mayores_10 += 1

# print(f"de los 5 numeros ingresados {conteo_mayores_10} son mayores que 10")

# #5 Haz un programa que sume todos los números pares del 1 al 100. Al final muestra el resultado de la suma

# suma_pares = 0
# for i in range(1, 100 + 1):
#     if i % 2 == 0:
#         suma_pares += i
# print(f"la suma de todos los numeros pares del 1 al 100 es: {suma_pares}. ")

#6 Haz un programa que genera la tabla de multiplicar de un número ingresado. Al final, muestra cuantos resultados de las multiplicaciones fueron mayores que 50, cuántos menores que 50 y cuántos iguales a 50.

numero = int(input("ingrese un numero: "))
conteo_mayores_50 = 0
conteo_iguales_50 = 0
print(f"Tabla de multiplicar del {numero}: ")
for i in range(1, 10 + 1):
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")
    if resultado > 50:
        conteo_mayores_50 += 1
    if resultado == 50:
        conteo_iguales_50 += 1
print(f"en la tabla de multiplicar de {numero} hay {conteo_mayores_50} resultados mayores que 50 y {conteo_iguales_50} resultados iguales a 50.")

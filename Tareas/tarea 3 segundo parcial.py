#1. Haz un programa que calcule cuántos números del 1 al 100 son divisibles entre 3 y entre 5.
print("Ejercicio 1")
contador = 0
for numero in range(1, 101):
    if numero % 3 == 0 and numero % 5 == 0:
        contador += 1
print(f"Hay {contador} numeros divisibles entre 3 y 5 del 1 al 100.")


#2. Haz un programa que solicite números al usuario hasta que ingrese un cero. Al final, imprime cuántos números positivos y negativos introdujo.
print("Ejercicio 2")
positivos = 0
negativos = 0
while numero != 0:
    numero = float(input("Ingrese un número (o 0 para terminar): "))
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"Números positivos ingresados: {positivos}")
print(f"Números negativos ingresados: {negativos}")


#3. Haz un programa que pida un número y muestre si es divisible entre 2, 3 o ambos.
print("Ejercicio 3")
numero = int(input("Ingrese un número: "))
if numero % 2 == 0 and numero % 3 == 0:
    print(f"El número {numero} es divisible entre 2 y 3.")
elif numero % 2 == 0:
    print(f"El número {numero} es divisible entre 2.")
elif numero % 3 == 0:
    print(f"El número {numero} es divisible entre 3.")
else:
    print(f"El número {numero} no es divisible ni entre 2 ni entre 3.")


#4. Haz un programa que sume todos los números impares del 1 al 50.
print("Ejercicio 4")
suma_impares = 0
for numero in range(1, 51):
    if numero % 2 != 0:
        suma_impares += numero
print(f"La suma de todos los números impares del 1 al 50 es: {suma_impares}.")

#5. Haz un programa que pida una edad, y dependiendo del rango, muestre una categoría: Menor de 13 años -> "Niño", 13 a 17 años -> "Adolescente", 18 a 64 años -> "Adulto", 65 o más -> "Adulto mayor".
print("Ejercicio 5")
edad = int(input("Ingrese su edad: "))
if edad < 13:
    print("Categoría: Niño")
elif 13 <= edad <= 17:
    print("Categoría: Adolescente")
elif 18 <= edad <= 64:
    print("Categoría: Adulto")
else:
    print("Categoría: Adulto mayor")

#6. Haz un programa que pida un número, y muestre si es primo o no.
print("Ejercicio 6")
numero = int(input("Ingresa un número: "))
contador = 0

if numero <= 1:
    print("No es primo.")
else:
    for i in range(1, numero + 1):
        if numero % i == 0:
            contador += 1

    if contador == 2:
        print("Es primo.")
    else:
        print("No es primo.")
        


#7. Haz un programa que pida un número, y calcule la suma de todos los números, desde el 1 hasta ese número. Por ejemplo, si ingresas 5, deberás sumar 1 + 2 + 3 + 4 +5.
print("Ejercicio 7")
numero = int(input("Ingrese un número: "))
suma_total = 0
for i in range(1, numero + 1):
    suma_total += i
print(f"La suma de todos los números desde 1 hasta {numero} es: {suma_total}.")


#8. Pide dos números y muestra todos los números entre ellos que sean múltiplos de 7.
print("Ejercicio 8")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
print(f"Números múltiplos de 7 entre {num1} y {num2}:")
for numero in range(num1, num2 + 1):
    if numero % 7 == 0:
        print(numero)


#9. Pide una cantidad de productos y su precio uno por uno, luego muestra el total con IVA del 16%.
print("Ejercicio 9")
cantidad_productos = int(input("Ingrese la cantidad de productos: "))
total_sin_iva = 0
for i in range(cantidad_productos):
    precio = float(input(f"Ingrese el precio del producto {i + 1}: "))
    total_sin_iva += precio
iva = total_sin_iva * 0.16
total_con_iva = total_sin_iva + iva
print(f"Total con iva del 16% es: {total_con_iva}.")


#10. Haz un programa que simule una calculadora básica con opciones de suma, resta, multiplicación y división, que se repita hasta que el usuario elija salir.
print("Ejercicio 10")
opcion = 0

while opcion != 5:
    print("Calculadora Básica")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = int(input("Elige una opción: "))

    if opcion >= 1 and opcion <= 4:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == 1:
            print("Resultado: ", num1 + num2)
        elif opcion == 2:
            print("Resultado: ", num1 - num2)
        elif opcion == 3:
            print("Resultado: ", num1 * num2)
        elif opcion == 4:
            if num2 != 0:
                print("Resultado: ", num1 / num2)
            else:
                print("Error: No se puede dividir entre cero.")
    elif opcion == 5:
        print("Saliendo de la calculadora... Hasta luego... ")
    else:
        print("Opción no válida. Intenta de nuevo.")
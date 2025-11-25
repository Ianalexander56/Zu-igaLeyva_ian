#Ejercicio 1: Haz un programa que pida una frase y cuenta cuantas letras tiene la frase, sin contar espacios.
print("Ejercicio 1")
Frase = input("Introduce una frase: ")
contador = 0
for caracter in Frase:
        contador += 1
print(F"La frase {Frase} tiene {contador} letras sin los espacios. ")

#Ejercicio 2: Pide una palabra y reemplaza todas las vocales por el caracter *
print("Ejercicio 2")
palabra = input("Introduce una palabra: ")
vocales = "aeiouAEIOU"
nueva_palabra = ""
for letra in palabra:
        if letra in vocales:
             nueva_palabra +="*"
        else:
             nueva_palabra += letra
print(F"la nueva palabra es: {nueva_palabra}")

#Ejercicio 3: Haz un programa que pida un numero entero N, y calcula la suma de todos los numeros del 1 al N
print("Ejercicio 3")
N = int(input("Introduce un numero entero N: "))
suma = 0
for i in range(1, N + 1):
       suma += i
print(F"La suma de todos los numeros del 1 al {N} es: {suma}")
       
#Ejercicio 4: Haz un programa que pida una palabra, y cuenta cuantas vocales tiene la palabra ingresada.
print("Ejercicio 4")
palabra = input("Introduce una palabra: ")
vocales = "aeiouAEIOU"
contador = 0
for letra in palabra:
       if letra in vocales:
              contador += 1
print(F"la palabra {palabra} tiene {contador} vocales.")

#Ejercicio 5: Haz un programa que pida al usuario solicitar 5 calificaciones, solo acepta numeros del 1 al 10 (si permite decimales). Almacena estas 5 calificaciones en un arreglo, y posteriormente calcula el promedio de las calificaciones, muestra solamente 2 decimales si el alumno tiene una calificacion promedio mayor que 6, imprime un mensaje de "aprobado", si tiene una calificacion menos impreme "reprobado", y si tiene una calicicacion de 10 imprimero "Exelente".
print("Ejercicio 5")
calificacion1 = float(input("Ingrese la primera calificacion: "))
calificacion2 = float(input("Ingrese la segunda calificacion: "))
calificacion3 = float(input("Ingrese la tercera calificacion: "))
calificacion4 = float(input("Ingrese la cuarta calificacion: "))
calificacion5 = float(input("Ingrese la quinta calificacion: "))
calificaciones = [calificacion1, calificacion2, calificacion3, calificacion4, calificacion5]
promedio = sum(calificaciones) / len(calificaciones)
if promedio > 6 and promedio < 10:
       print(F"el alumno esta aprobado con un promedio de: {promedio}")
elif promedio < 6:
       print(F"el alumno esta reprobado con un promedio de: {promedio}")
elif promedio == 10:
       print("felicidades, Exelente")

#Ejercicio 6: Pide al usuario ingresar 10 productos y almacenalos en una lista. Luego muestra la lista ordenada alfabeticamente
print("Ejercicio 6")
productos = []
for i in range(10):
       producto = input("Ingrese el nombre del producto: ")
       productos.append(producto)
       productos.sort()
print("La lista de productos ordenada alfabeticamente es: ")
for producto in productos:
       print(producto)

#Ejercicio 7: Haz un programa que pida un numero y determina si es par o impar
print("Ejercicio 7")
numero = int(input("Ingrese un numero: "))
if numero % 2 == 0:
       print(F"El numero {numero} es par")
else:
       print(F"el numero {numero} es impar")

#Ejercicio 8: Haz un programa que pida un nombre y apellido, posteriormente muestra un mensaje con un saludo, y se muestre el nombre y apellido ingresados
print("Ejercicio 8")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
print(F"Bienvenido {nombre} {apellido} ")  







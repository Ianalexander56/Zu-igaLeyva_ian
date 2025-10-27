#Sintaxis condicionales

#if condicion:
#   intrucciones si la condicion es verdadera
#elif otra condicion:
# intrucciones si la otra condicion es verdadera
#else:
# instrucciones si ninguna condicion es verdadera 

# Ejercicio 1: Programa que pida un numero y muestre si es positivo, negativo o cero.
numero=float(input("Ingrese un numero"))

if numero>0: 
    print("Bloque if ejecutado.")
    print("El numero es positivo.")
elif numero<0:
    print("Bloque elif ejecutado.")
    print("El numero es negativo")
else:
    print("Bloque else ejecutado.") 
    print("El numero es cero") 

print("------------------------------") 

# if condicion:
#  if condicion_anidada:
#   intrucciones si la condicion_anidada es verdadera
#   else:
# instrucciones si la condicion_anidada es falsa

# Ejercicio 2: Programa que pida dos numeros y muestre cual es mayor o si son iguales.

num1= float(input("Ingrese el primer numero:"))
num2= float(input("Ingrese el segundo numero"))

if num1>num2:
    print("El primer numero es mayor.")
elif num1<num2: #num2 > num1
    print("El segundo numero es mayor.")
else:
    print("Ambos numeros son iguales.")

print("-------------------------")

#Ejercicio 3: Haz un programa que pida una calificacion del 0 al 10 y muestre si esta aprobado o reprobado. Toma en cuenta una calificacion mayor o igual a 6 como aprobatoria.

nombreAlumno=input("Ingrese el nombre del alumno:")
calificacion=float(input("Ingrese la calificacion del alumno(0-10):"))

if calificacion>= 6:
    print(f"El alumno {nombreAlumno} esta aprobado.")
else:
    print(f"El alumno {nombreAlumno} esta reprobado.")

print("-------------------------")

#Ejercicio 4: Haz un programa que pida la edad de una persona y muestre si puede votar(mayor o igual a 18 años) o no

nombre= input("Ingrese el nombre de la persona:")
edadPersona= int(input("Ingrese su edad."))

if edadPersona >= 18:
    print(f"{nombre}tiene{edadPersona}años y puede votar.")
else:
    print(f"{nombre}tiene{edadPersona}años y no puede votar.")
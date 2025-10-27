#for variable in interable
# bloque de codigo

#funcion range (inicio ,fin, paso)

#ejemplo usandro range, se imprimira todos los pare del 0 al 8
# for i in range(0, 10, 2):
#      print(i)

# #ejercicio 1: Haz un programa que muestre los numeros de 1 al 10
# print("Numeros del 1 al 20:")
# for numero in range(1, 21):
#      print(numero)

#Ejercicio 2: Haz un programa que muestre la tabla de multiplicar de un numero dado por el usuario (del 1 al 10)

numero_usuario = int(input("Introduce un numero: "))
print(f"tabla de multiplicar del {numero_usuario}: ")
for i in range(1, 11):
     resultado = numero_usuario * i
     print(f"{numero_usuario} * {i} = {resultado}")
     

     
     

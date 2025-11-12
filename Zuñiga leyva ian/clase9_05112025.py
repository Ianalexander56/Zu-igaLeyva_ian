palabra = "palabra ejmplo"

for letra in palabra:
    print(letra)

#Ejercicio 3: Haz un programa que pida nombre y apellido. Muestra en pantalla en formato apellido, Nombre con cada palabra iniciando en mayuscula
nombre = input("Escribe tu nombre: ")
apellido = input("Escribe tu apellido: ")
nombre_completo = apellido + ", " + nombre

print(f"{apellido.capitalize()}, {nombre.capitalize()}") #Aqui usamos cadena formateadas para mostrar el resultado, todo el trato de mayusculas se hace en esta linea
print(nombre_completo.title()) # Aqui usamos title para convertir la primera letra de cada palabra en mayuscula, trabajamos con la variable creada anteriormente

#Ejercicio 4: Pide una frase y una letra. Muestra cuantas veces aparece esa letra en la frase sin distinguir entre mayuculas y minusculas

frase = input("Escribe una frase: ")
letra =input("Escribe la letra que deseas buscar: ")
frase_formateada = frase.strip().lower() #Limpiamos espacios y convertimos a mayusculas
letra_formateda = letra.strip().lower() #Limpiamos espacios y convertimos a minusculas

conteo_letra = frase_formateada.count(letra_formateda) #Contar las apariciones de la letra ingresida por el usuario en la frase

print(F"la letra '{letra}' aparece {conteo_letra} veces en la frase: {frase} ")

#Ejercicio 5: Pide una frase y reempleaza todas las vocales 'a' por '@' y muestra el resultado.
frase = input("Escribe una frase: ")
frase_formateada = frase.strip().lower() #Limpiamos espacios y convertimos a minusculas
frase_modificada = frase_formateada.replace("a", "@") #Reemplazamos todas las 'a' por '@'
print("Frase modificada:", frase_modificada)

#Ejercicio 6: Pide un texto y extrae los primeros 10 caracteres. Si el texto tiene menos de 10 caracteres, muestra el texto completo.
texto = input("Escribe un texto o frase: ")
if len(texto) <= 10:
    print(F"El texto completo es: {texto}")
else:
    texto_diez_caracteres = texto[:10]
    print(F"Los primeros 10 caracteres son: {texto_diez_caracteres}")

#LISTAS DE PYTHON  
lista1 = [10, 30, 20, 50, 5, 15]
lista2 = ["manzana", "banana", "fresa", "pera", "naranja", 4, 6.6, True] #Lista con diferentes tipos de datos

print(lista1)
print(lista2)

#Recorrido de listas
for elemento in lista1:
    print(elemento)

for elemento in lista2:
    print(elemento)

#Llenado de listas vacias
lista3 = [] #Lista vacia
# Llenar la lista con datos ingresados por el usuario
for i in range(11):
    numero = int(input("Ingresa un numero entero: "))
    lista3.append(numero) #Agregar el numero ingresado a la lista (append agrega un elemnto al final de la lista)

print("Lista ya full bro:", lista3)
print(len(lista3)) #Imprime la longitud de la lista
print(sum(lista3)) #Imprime la suma de todos los elemento de la lista
lista3.reverse() #Invierte el orden de los elementos de la lista
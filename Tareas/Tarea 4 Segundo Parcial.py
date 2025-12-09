#Ejercicio 1. Pide una frase, divídela en palabras y guarda una lista solo las que tengan más de 5 letras. Muestra la lista resultante.
print("Ejercicio 1")
frase = input("Introduce una frase: ")
palabras = frase.split()
palabras_mas_de_5 = []
for palabra in palabras:
    if len(palabra) > 5:
        palabras_mas_de_5.append(palabra)
print(palabras_mas_de_5)

#Ejercicio 2. Haz un programa que pida una frase y cuenta cuántas veces aparece cada palabra. Por ejemplo "Esta es una prueba", "Esta" aparece una vez, "es", una vez, "una", una vez, etc...
print("Ejercicio 2")
frase = input("Introduce una frase: ")
palabras = frase.split()
contador_palabras = {}
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1
print(contador_palabras)

#Ejercicio 3. Haz un programa que pida al usuario una contraseña. Verifica que: La contraseña tenga al menos 8 caracteres, y que contenga al menos una mayúscula y un número.
print("Ejercicio 3")
contraseña = input("Introduce una contraseña: ")
tiene_mayuscula = any(c.isupper() for c in contraseña)
tiene_numero = any(c.isdigit() for c in contraseña)
es_valida = len(contraseña) >= 8 and tiene_mayuscula and tiene_numero
if es_valida:
    print("Contraseña válida")
else:
    print("Contraseña inválida. Debe tener al menos 8 caracteres, una mayúscula y un número.")


#Ejercicio 4. Haz un programa que pida un texto y una palabra. Si la palabra está en el texto, muestra cuántas veces aparece.
print("Ejercicio 4")
texto = input("Introduce un texto: ")
palabra_buscar = input("Introduce una palabra a buscar: ")
contador = texto.split().count(palabra_buscar)
print(f"La palabra '{palabra_buscar}' aparece {contador} veces en el texto.")



#Ejercicio 5. Pide al usuario una lista de palabras (separadas por comas, por ejemplo Hola, Mario, Python, Programación). Elimina los elementos repetidos y los que sean menores a 3 letras. Muestra la nueva lista e imprímela en pantalla. 
print("Ejercicio 5")
entrada = input("Introduce una lista de palabras separadas por comas: ")
palabras = entrada.split(",")
palabras_filtradas = []

for palabra in palabras:
    palabra_limpia = palabra.strip()
    
    if len(palabra_limpia) >= 3:
        if palabra_limpia not in palabras_filtradas:
            palabras_filtradas.append(palabra_limpia)

print(palabras_filtradas)

#Ejercicio 6. Crea un diccionario con clave y valor producto : precio. Luego, pide una lista de productos comprados y muestra el total de la compra. Si el producto no existe, muestra una advertencia.
print("Ejercicio 6")
productos = {
    "manzana": 9,
    "banana": 7,
    "naranja": 5,
    "leche": 22,
    "pan": 10
}
entrada = input("Introduce una lista de productos comprados separados por comas: ")
productos_comprados = entrada.split(",")
total = 0
for producto in productos_comprados:
    producto = producto.strip()
    if producto in productos:
        total += productos[producto]
    else:
        print(f"Advertencia: El producto '{producto}' no existe.")
print(f"Total de la compra: ${total}")


#Ejercicio 7. Haz un programa en Python que pida repetidamente el nombre de una persona y su respuesta ("Si" o "No"). Guarda cada respuesta en un diccionario, donde la clave sea el nombre y el valor la respuesta. El programa debe terminar cuando el usuario escriba "Fin" como nombre. Al finalizar, muestra cuántas personas respondieron "Si", y cuántas respondieron "No"
print("Ejercicio 7")
respuestas = {}
contador_si = 0
contador_no = 0
while True:
    nombre = input("Introduce el nombre de una persona (o 'Fin' para terminar): ")
    if nombre.lower() == "fin":
        break
    respuesta = input("Introduce la respuesta ('Si' o 'No'): ")
    respuestas[nombre] = respuesta
for i in respuestas.values():
    if i.lower() == "si":
      contador_si += 1
    elif i.lower() == "no":
      contador_no += 1
print(f"Cantidad de respuestas 'Si': {contador_si}")
print(f"Cantidad de respuestas 'No': {contador_no}")


#Ejercicio 8. Haz un programa que pida una palabra y verifique si inicia con una vocal.
print("Ejercicio 8")
palabra = input("Introduce una palabra: ")
if palabra[0].lower() in 'aeiou':
    print("La palabra inicia con una vocal.")
else:
    print("La palabra no inicia con una vocal.")


#Ejercicio 9. Haz un programa que pida el nombre de un contacto y su teléfono, y los agregue a un diccionario.
print("Ejercicio 9")
contactos = {}
nombre = input("Introduce el nombre del contacto: ")
telefono = input("Introduce el teléfono del contacto: ")
contactos[nombre] = telefono
print("Contacto agregado:", contactos)


#Ejercicio 10. Haz un programa que pida 5 nombres y luego pregunte uno; si está en la lista, muestra “Encontrado”.
print("Ejercicio 10")
nombres = []
for _ in range(5):
    nombre = input("Introduce un nombre: ")
    nombres.append(nombre)
nombre_buscar = input("Introduce un nombre para buscar: ")
if nombre_buscar in nombres:
    print("Encontrado")
else:
    print("No encontrado")







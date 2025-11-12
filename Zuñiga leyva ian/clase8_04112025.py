nombre = "Ian Alexander Zuñiga Leyva"
cadena2 = "hola amigos me llamo ian zuñiga pero me llamar alex"
cadena3 = "           Que onda bro           "
cadena4 = "esto es una cadena bro"
cadena5 = "esta es otra mongol"

print(len(nombre)) #imprime la logitud de la cadena

print(nombre.upper()) #convierre la cadena a mayusculas

print(nombre.lowe()) #convierte la cadena en minusculas

print (cadena2.capitalize()) #convierte el primer caracter a mayuscula y el resto a minusculas

print(cadena2.title()) # convierte la primera letra de cada palabra a mayuscula 

print(cadena3)
print(cadena3.strip()) # Elimina los espacios en blanco al inicio y al final de la cadena 

cadenaNueva = cadena4 + cadena5
print(cadenaNueva) #concatenacion de cadenas

cadenaMultiplicada = cadena4 * 5
print(cadenaMultiplicada) #multiplicacion de cadenas

print(cadena4.replace("a", "s")) #reemplaza todas la apariciones de "A" po "S"

cadena6 = "Que onda mongoles ¿todo bien?"
indice = cadena6.find("onda") #busca la posicion de la ultima aparicion de "onda"
print(indice) # Imprime la posicion de la primera aparicion de "onda"

indiceUltimo = cadena6.rfind("onda") # Busca la posicion de la ultima aparicion de "onda"
print(indiceUltimo) #Imprime la posicion de la ultima aparicion de "onda"

cadena7 = "blue label de jonnhy walker"
conteo = cadena7.count("blue") #Cuenta cuantas veces aparece "blue" en la cadena
print(conteo) #Imprime el conteo de "blue"

print(cadena7.startswith("label")) #Verifica si la cadena comieza con "label"
print(cadena7.endswith("walker")) #Verifica si la cadena termina con "walker"

#Sintaxis de slicing cadena [incio:fin:paso]

cadena8 = "hola como estas"
print(cadena8[0:4]) #Imprime "Hola"
print(cadena8[:4]) #Imprime "Hola"
print(cadena8[4:9]) #Imprime "a to"
print(cadena8[5:]) #Imprime "a todos"
print(cadena8[-2:]) #Imprime "os"
print(cadena8[::2]) #Imprime "hl atds"
print(cadena8[::-1]) #Imprime la cadena al reves "satse omoc aloH"

#Ejercicio 1: pide una frase y muestra la misma frase sin espacios al inicio y al final con todas las letras en minusculas
frase = input("Escribir una frase: ")
fraseLimpia = frase.strip().lower()
print(fraseLimpia)

#Ejercicio 2: pide una palabra y comprueba si es un palidromo 
palabra = input("Escribir una palabra: ")
palabra_invertida = palabra[::-1]
if palabra.lower() == palabra_invertida.lower():
    print("La palabra es un palindromo")
else:
    print("La palabra no es un polindromo")
    
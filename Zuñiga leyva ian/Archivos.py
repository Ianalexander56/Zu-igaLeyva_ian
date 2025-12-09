#En Python existen los siguientes modos de escritura y lectura de archivos:
#'r' - Modo de lectura (read): Este es el modo predeterminado. Abre un archivo para leer su contenido. Si el archivo no existe, se genera un error.
#'w' - Modo de escritura (write): Abre un archivo para escribir en él. Si el archivo ya existe, su contenido se borra. Si el archivo no existe, se crea uno nuevo.
#'a' - Modo de anexado (append): Abre un archivo para agregar contenido al final del mismo. Si el archivo no existe, se crea uno nuevo.
#'r+' - Modo de lectura y escritura (read and write): Abre un archivo para leer y escribir en él. El archivo debe existir; de lo contrario, se genera un error.
#'w+' - Modo de escritura y lectura (write and read): Abre un archivo para escribir y leer. Si el archivo ya existe, su contenido se borra. Si el archivo no existe, se crea uno nuevo.
#'a+' - Modo de anexado y lectura (append and read): Abre un archivo para agregar contenido al final y leerlo. Si el archivo no existe, se crea uno nuevo.

#apertura de archivo
# open ("ruta/del/archivo.txt", "modo")

#cerrar el archivo
# archivo.close()

#podemos abrir el archivo haciendo uso de 'with', el cual cierra el archivo de manera automatica al finalizar el bloque de codigo 
#with open("ruta/del/archivo.txt", "modo") as archivo:
#     #operaciones con el archivo

with open("archivos.txt", "r") as archivo:
    contenido = f.read() # leer todo el contenido del archivo, y lo va a almacenar en la variable contenido
print(contenido) 

with open("archivo.txt", "r") as f:
    for linea in f: #leer el archivo linea por linea
        print(linea.strip()) #Imprimir cada linea espacios adicionales

with open("archivo2.txt", "w") as f:
    f.write("Esta es una nueva linea escrita en el archivo .\n") 
    f.write("Otra linea añadida al archivo.\n")

with open("archivo3.txt", "a") as f:
    f.write("Esta linea se agrega al final del archivo existente.\n")

with open("archivo.txt", "r+") as f:
    contenido = f.read()
    f.write("\nEsta linea se ha añadido al final del archivo usando r+.\n") 

with open("archivo2.txt", "w+") as f:
    f.write("Escribiendo en archivo2 usando w+.\n")
    f.seek(0)
    contenido = f.read()
    print(contenido)
    


#funcion para buscar estudiante por medio del apellido
def buscar_estudiante_apellido(lista_estudiantes):
    apellido_buscar = input("Ingrese el apellido del estudiante que desee buscar: ")
    for estudiante in lista_estudiantes:
        if estudiante["apellido"].lowe() == apellido_buscar.lowe():
            print(F"Estudiante encontrado: {estudiante["nombre"]} {estudiante["apellido"]}")


#Funcion para calcular el promedio del grupo
def calcular_promedio_grupo(lista_estudiantes):
    suma_promedios = 0
    for estudiante in lista_estudiantes:
        suma_promedios += estudiante["promedio"]
    promedio_grupo = suma_promedios / len(lista_estudiantes)  
    print(F"El promedio del grupo es: {promedio_grupo}")


#Funcion para ordenar estudiantes por promedio (de la calificacion mas baja a la mas alta)
promedio = lambda estudiante: estudiante["Promedio"]
def ordenar_estudiantes_por_promedio(lista_estudiantes):
    lista_ordenada = sorted(lista_estudiantes)
    print("Estudiantes ordenados por promedio (de menor a mayor):")
    for estudiante in lista_ordenada:
        print(f"{estudiante['nombre']} {estudiante['apellido']} - Promedio: {estudiante['promedio']}")




import os
from datetime import datetime #Sirve para que nos dé la fecha y hora
from rich.console import Console
from rich.table import Table
os.system("cls") #Sirve para limpiar la pantalla

#Todas las variables que debe tener el material
titulo = ""
curso = ""
autor = ""
anio = 0
modalidad = ""
nivel = ""
grado = ""
idioma = ""
tipo_de_archivo = ""
id_material = 0
fecha_y_hora_subida = ""

#Tuplas para las variables que van a tener valores predefinidos
MODALIDADES = ("Básica regular", "Básica alternativa", "Básica especial")
NIVELES = ("Inicial", "Primaria", "Secundaria", "Otros")
GRADOS = ("1ro", "2do", "3ro", "4to", "5to", "6to", "Otros")
IDIOMAS = ("Castellano", "Quechua", "Aymara", "Inglés", "Otros")
CURSOS = ("Comunicación", "Matemáticas", "Ciencias", "Inglés", "Otros")
TIPOS_DE_ARCHIVO = ("PDF", "Word", "Excel", "PPT", "Video")

#Matriz que va a contener todos los materiales creados, llené el material con data de ejemplo
matriz_materiales = [
    ["Matemáticas para Principiantes", "Matemáticas", "John Doe", "2022", "Básica regular", "Primaria", "4to", "Castellano", "PDF", "1", "19/07/2023 10:30"],
    ["Ciencias Naturales Avanzadas", "Ciencias", "Jane Smith", "2021", "Básica especial", "Secundaria", "2do", "Inglés", "Word", "2", "19/07/2023 11:45"],
    ["Aprender a Programar con Python", "Otros", "Albert Einstein", "2023", "Básica alternativa", "Otros", "Otros", "Aymara", "Video", "3", "19/07/2023 14:20"],
    ["Introducción a la Literatura", "Comunicación", "Emily Dickinson", "2023", "Básica regular", "Secundaria", "3ro", "Quechua", "PDF", "4", "19/07/2023 16:05"],
    ["Historia Universal", "Otros", "William Shakespeare", "2022", "Básica especial", "Primaria", "6to", "Castellano", "PPT", "5", "19/07/2023 18:15"],
    ["Inglés Intermedio", "Inglés", "Michael Johnson", "2023", "Básica regular", "Secundaria", "4to", "Inglés", "PDF", "6", "20/07/2023 09:00"],
    ["Arte y Creatividad", "Otros", "Pablo Picasso", "2023", "Básica especial", "Primaria", "5to", "Castellano", "Word", "7", "20/07/2023 11:30"],
    ["Geometría Avanzada", "Matemáticas", "Alberto García", "2022", "Básica regular", "Secundaria", "3ro", "Castellano", "Video", "8", "20/07/2023 14:15"],
    ["Biología para Todos", "Ciencias", "Marie Curie", "2023", "Básica alternativa", "Otros", "Otros", "Castellano", "PDF", "9", "20/07/2023 16:40"],
    ["Introducción a la Filosofía", "Otros", "Socrates", "2022", "Básica especial", "Secundaria", "1ro", "Castellano", "PPT", "10", "20/07/2023 19:00"],
]

#Definiendo las opciones que va a tener el menú principal
opciones_de_menu = {
    1: 'Ingreso de materiales nuevos',
    2: 'Visualización de materiales educativos',
    3: 'Edición de materiales educativos',
    4: 'Salir del programa',
}

#Definiendo la función para imprimir el menú y todas sus opciones definidas en el diccionario anterior^
def imprimir_menu():
    print('==============================================')
    print('\tAPRENDO EN CASA')
    print('==============================================')
    for key in opciones_de_menu.keys():
        print (key, '--', opciones_de_menu[key] )

#Definiendo la función para la opción 1 (Ingreso de materiales)
def opcion_1():
     os.system("cls")
     print('==============================================')
     print('\tINGRESO DE MATERIALES')
     print('==============================================')
     titulo = str(input('Ingrese el título del material:\n'))
     os.system("cls")
     print('CURSOS:')
     for i in range(0, len(CURSOS)):
         print("{} -- {}".format(i+1, CURSOS[i]))
     curso = CURSOS[int(input('Seleccione el curso del material:\n'))-1]
     os.system("cls")
     autor = str(input('Ingrese el autor del material:\n'))
     os.system("cls")
     anio = int(input('Ingrese el año del material:\n'))
     os.system("cls")
     print('MODALIDADES DE ESTUDIO:')
     for i in range(0, len(MODALIDADES)):
         print("{} -- {}".format(i+1, MODALIDADES[i]))
     modalidad = MODALIDADES[int(input('Elija una de las modalidades mostradas arriba:\n'))-1]
     os.system("cls")
     print('NIVELES DE ESTUDIO:')
     for i in range(0, len(NIVELES)):
         print("{} -- {}".format(i+1, NIVELES[i]))
     nivel = NIVELES[int(input('Elija uno de los niveles mostrados arriba:\n'))-1]
     os.system("cls")
     print('GRADOS:')
     for i in range(0, len(GRADOS)):
         print("{} -- {}".format(i+1, GRADOS[i]))
     grado = GRADOS[int(input('Elija uno de los grados mostrados arriba:\n'))-1]
     os.system("cls")
     print('IDIOMAS:')
     for i in range(0, len(IDIOMAS)):
         print("{} -- {}".format(i+1, IDIOMAS[i]))
     idioma = IDIOMAS[int(input('Seleccione el idioma del material:\n'))-1]
     os.system("cls")
     print('TIPOS DE ARCHIVO:')
     for i in range(0, len(TIPOS_DE_ARCHIVO)):
         print("{} -- {}".format(i+1, TIPOS_DE_ARCHIVO[i]))
     tipo_de_archivo = TIPOS_DE_ARCHIVO[int(input('Seleccione el tipo de archivo del material:\n'))-1]
     os.system("cls")
     #Este bloque de código sirve para darles un identificador que vaya aumentando de 1 en uno
     if len(matriz_materiales) == 0:
         id_material = 1
     else:
         id_material = int(matriz_materiales[-1][9]) + 1 
     #Esta línea es para conseguir el día y la hora actual
     fecha_y_hora_subida = datetime.now().strftime("%d/%m/%Y %H:%M")
     #El material se añade a la matriz
     matriz_materiales.append([
         titulo.title(), #El .title() es para que la primera letra de cada palabra esté con mayúscula
         curso,
         autor.title(),
         str(anio),
         modalidad,
         nivel,
         grado,
         idioma,
         tipo_de_archivo,
         str(id_material),
         fecha_y_hora_subida
     ])
     os.system("cls")
     print("Se añadió el material con éxito.")

#Definiendo la función para la opción 2 (Visualización de materiales) rich
def opcion_2(matriz):
     os.system("cls")
     #El siguiente bloque de código es la sintaxis para llenar la tabla utilizando la librería 'Rich'
     console = Console()
     tabla = Table(title="VISUALIZACIÓN DE TODOS LOS MATERIALES")
     columnas = ["Título", "Curso", "Autor", "Año", "Modalidad", "Nivel", "Grado", "Idioma", "Tipo de archivo", "ID", "Fecha y hora de subida"]
     for columna in columnas:
         tabla.add_column(columna)
     for fila in matriz:
         tabla.add_row(*fila)
     console.print(tabla)
     
#Definiendo la función para la opción 3 (Edición de materiales)
def opcion_3():
     os.system("cls")
     print('==============================================')
     print('\tEDICIÓN DE MATERIALES')
     print('==============================================')
     caracteristicas_del_material = ("Título", "Curso", "Autor", "Año", "Modalidad", "Nivel", "Grado", "Idioma","Tipo de archivo", "ID")

     ID_elegido = int(input("Escriba el ID del Material a Editar:\n"))
     if ID_elegido>len(matriz_materiales):
         print("El ID del material no existe")
     else:
          print("Este es el material elegido:")
          for i in range(0, len(caracteristicas_del_material)):
              print("{}. {}: {}". format(i+1, caracteristicas_del_material[i], matriz_materiales[ID_elegido-1][i]))
          caracteristica_a_editar = int(input("Elija una de las características a editar"))
          if caracteristica_a_editar>len(caracteristicas_del_material)+1:
              print("La opción no es válida")
          else:
              valor_a_editar = str(input("Indique el nuevo valor de la característica {}". format(caracteristicas_del_material [caracteristica_a_editar-1])))
              matriz_materiales[ID_elegido-1][caracteristica_a_editar-1] = valor_a_editar
              print("¡¡El valor a sido editado con éxito!!")
    
#Ejecución del programa, se llama a las opciones definidas arriba de acuerdo a la selección del usuario
if __name__=='__main__':
    while(True):
        imprimir_menu()
        opcion = ''
        try:
            opcion = int(input('Escriba su elección: '))
        except:
            os.system("cls")
            print('ERROR: Por favor ingrese un número de acuerdo a las opciones mostradas ...')
        #De acuerdo a la elección ingresada se va a ejecutar una de las funciones.
        if opcion == 1:
           opcion_1()
        elif opcion == 2:
            opcion_2(matriz_materiales)
        elif opcion == 3:
            opcion_3()
        elif opcion == 4:
            os.system("cls")
            print('Gracias por utilizar nuestro programa. Hasta luego!')
            exit()
        else:
            os.system("cls")
            print('Opción inválida, por favor ingrese un número del 1 al 4.')
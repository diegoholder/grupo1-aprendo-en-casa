import os
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

#Tuplas para las variables que van a tener valores predefinidos
MODALIDADES = ("Básica regular", "Básica alternativa", "Básica especial")
NIVELES = ("Inicial", "Primaria", "Secundaria", "Otros")
GRADOS = ("1ro", "2do", "3ro", "4to", "5to", "6to", "Otros")
IDIOMAS = ("Castellano", "Quechua", "Aymara", "Inglés", "Otros")
CURSOS = ("Comunicación", "Matemáticas", "Ciencias", "Inglés")

#Lista que va a contener todos los materiales creados (los materiales son diccionarios)
lista_materiales = []

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
     for i in CURSOS:
         indice = CURSOS.index(i)+1
         print("{} -- {}".format(indice, i))
     curso = CURSOS[int(input('Seleccione el curso del material:\n'))-1]
     os.system("cls")
     autor = str(input('Ingrese el autor del material:\n'))
     os.system("cls")
     anio = int(input('Ingrese el año del material:\n'))
     os.system("cls")
     print('MODALIDADES DE ESTUDIO:')
     for i in MODALIDADES:
         indice = MODALIDADES.index(i)+1
         print("{} -- {}".format(indice, i))
     modalidad = MODALIDADES[int(input('Elija una de las modalidades mostradas arriba:\n'))-1]
     os.system("cls")
     print('NIVELES DE ESTUDIO:')
     for i in NIVELES:
         indice = NIVELES.index(i)+1
         print("{} -- {}".format(indice, i))
     nivel = NIVELES[int(input('Elija uno de los niveles mostrados arriba:\n'))-1]
     os.system("cls")
     print('GRADOS:')
     for i in GRADOS:
         indice = GRADOS.index(i)+1
         print("{} -- {}".format(indice, i))
     grado = GRADOS[int(input('Elija uno de los grados mostrados arriba:\n'))-1]
     os.system("cls")
     print('IDIOMAS:')
     for i in IDIOMAS:
         indice = IDIOMAS.index(i)+1
         print("{} -- {}".format(indice, i))
     idioma = IDIOMAS[int(input('Seleccione el idioma del material:\n'))-1]
     os.system("cls")
     lista_materiales.append([
         titulo,
         curso,
         autor,
         anio,
         modalidad,
         nivel,
         grado,
         idioma,
     ])
     os.system("cls")
     print("Se añadió el material con éxito.")

#Definiendo la función para la opción 2 (Visualización de materiales)
def opcion_2():
     os.system("cls")
     print('==============================================')
     print('\tVISUALIZACIÓN DE MATERIALES')
     print('==============================================')
     print(lista_materiales)

#Definiendo la función para la opción 3 (Edición de materiales)
def opcion_3():
     os.system("cls")
     print('==============================================')
     print('\tEDICIÓN DE MATERIALES')
     print('==============================================')

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
            opcion_2()
        elif opcion == 3:
            opcion_3()
        elif opcion == 4:
            os.system("cls")
            print('Gracias por utilizar nuestro programa. Hasta luego!')
            exit()
        else:
            os.system("cls")
            print('Opción inválida, por favor ingrese un número del 1 al 4.')
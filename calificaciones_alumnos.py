# Se crea una lista vacía llamada lista_calificaciones que servirá 
# para almacenar los nombres de los alumnos y sus respectivas calificaciones.
lista_calificaciones = []

print("""
Agregar un nuevo alumno (1)
Ver los alumnos y las calificaciones (2)
Salir (S)
""")

while True:
    menu = input("Ingresa una opcion: ")
    
    # Si el usuario no ingresa ninguna opción, se muestra un mensaje de error.
    if menu == "":
        print("La opcion esta vacia, ingresa una opcion valida")
        
    # Si el usuario selecciona la opción "1", 
		# se le solicita que ingrese el nombre del alumno y el número de calificaciones que desea ingresar.
    elif menu == "1":
        nombre_alumno = input("Ingresa el nombre del alumno: ")
        if nombre_alumno == "":
            print("Dato vacio, ingrese un nombre")
        else:
            numero_calificaciones = input("Cuantas calificaciones desea ingresar: ")
            
            # Si el usuario ingresa un número válido de calificaciones, se utiliza un bucle "for" para solicitar 
						# cada calificación y agregarla a la lista de calificaciones del alumno.
            if numero_calificaciones.isdigit():
                calificaciones_alumno = []
                for i in range(int(numero_calificaciones)):
                    try:
                        calificacion = int(input("Ingrese la calificacion del alumno: "))
                        calificaciones_alumno.append(calificacion)
                    except ValueError:
                        print("Dato incorrecto, ingrese de nuevo una calificacion")
                        
                # Se agrega una lista con el nombre del alumno y sus calificaciones a la lista general de calificaciones.
                lista_calificaciones.append([nombre_alumno, calificaciones_alumno])
            else:
                print("Dato incorrecto, ingrese un numero entero para las calificaciones")
                
    # Si el usuario selecciona la opción "2", se verifica si hay algún alumno registrado 
		# y se muestra el nombre de cada alumno junto con su promedio de calificaciones.
    elif menu == "2":
        if lista_calificaciones:
            for alumno in lista_calificaciones:
                nombre_alumno = alumno[0]
                calificaciones_alumno = alumno[1]
                promedio = sum(calificaciones_alumno)/len(calificaciones_alumno)
                print(f"{nombre_alumno} : promedio {promedio}")
        else:
            print("No hay alumnos registrados")
            
    # Si el usuario selecciona la opción "S" (o "s"), se rompe el bucle y se sale del programa.
    elif menu.lower() == "s":
        break
    
    # Si el usuario ingresa una opción inválida, se muestra un mensaje de error.
    else:
        print("Dato incorrecto, ingrese una opcion valida")



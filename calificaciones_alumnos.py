# Programa de promedio de calificaciones de alumnos

# Crear una lista vacía para almacenar la información de los alumnos
lista = []
# Inicializar un contador para llevar el registro de la cantidad de alumnos ingresados
alumnos = 0

# Iniciar un ciclo while infinito para que el programa siga ejecutándose hasta que el usuario decida finalizarlo
while True:
    # Solicitar al usuario que ingrese una opción: 1 para ingresar usuarios, 2 para finalizar el programa
    opciones = input("Ingrese (1) para ingresar usuarios, (2) para finalizar programa: ")

    # Si el usuario ingresó '1', continuar con el proceso de ingreso de usuarios
    if opciones == '1':
        # Solicitar al usuario que ingrese la cantidad de alumnos que desea ingresar
        numero_alumnos = input("Ingrese la cantidad de alumnos que desea ingresar: ")

        # Verificar si el valor ingresado es numérico
        if numero_alumnos.isnumeric():
            # Convertir el valor ingresado a un entero
            numero_alumnos = int(numero_alumnos)
            # Iniciar un ciclo for para iterar por cada uno de los alumnos que el usuario desea ingresar
            for numero_alumno in range(1, numero_alumnos+1):
                # Iniciar un ciclo while para validar que se ingresen los datos correctamente
                while alumnos < numero_alumno:
                    # Solicitar al usuario que ingrese el nombre del alumno y validar que solo contenga letras
                    nombre_alumno = input("Ingrese el nombre del alumno: ").capitalize()
                    if nombre_alumno.isnumeric() or nombre_alumno == "":
                        print("El nombre del alumno no puede estar vacío y debe contener solo letras")
                        continue
                    else:
                        # Solicitar al usuario que ingrese la primera calificación del alumno y validar que sea numérica
                        primera_calificacion = input(f"Ingrese la primera calificacion de {nombre_alumno}: ")
                        if primera_calificacion.isnumeric():
                            try:
                                # Convertir la calificación ingresada a un entero
                                primera_calificacion = int(primera_calificacion)
                                # Solicitar al usuario que ingrese la segunda y tercera calificación del alumno y convertirla a un entero
                                segunda_calificacion = int(input(f"Ingrese la segunda calificacion de {nombre_alumno}: "))
                                tercera_calificacion = int(input(f"Ingrese la tercera calificacion de {nombre_alumno}: "))
                                # Crear una lista con el nombre y las tres calificaciones del alumno y agregarla a la lista general de alumnos
                                lista_alumno = [nombre_alumno, primera_calificacion, segunda_calificacion, tercera_calificacion]
                                lista.append(lista_alumno)
                                # Incrementar el contador de alumnos ingresados
                                alumnos += 1

                            except ValueError:
                                print("Calificación no válida, ingrese una calificación correcta")
                                continue 
                        else:
                            print("Calificación no válida, debe haber una calificación")
                            continue
        else:
            print("Vuelva a ingresar el numero de alumnos, Dato no valido")
            continue
    # Si el usuario ingresó '2', finalizar el programa
    elif opciones == "2":
        print("El programa ha finalizado")
        exit()
    # Si el usuario ingresa una opción inválida, se muestra un mensaje de error y se continua con el loop
    else:
        print("Valor invalido, ingrese una opción válida")
        continue
    # Loop para calcular y mostrar el promedio de cada alumno
    for lista_alumnos in lista:
        nombre = lista_alumnos[0]
        calificaciones = lista_alumnos[1:]
        promedio = sum(calificaciones) / len(calificaciones)
        print(f"la calificacion promedio de {nombre} es: {promedio}.")


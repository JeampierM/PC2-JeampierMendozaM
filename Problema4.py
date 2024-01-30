listaAlumnos = []

n = int(input("Ingrese la cantidad de alumnos: "))

for i in range(n):
    nombreAlumno = input(f"Ingrese el nombre del alumno {i + 1}: ")

    calificaciones = []
    for j in range(3):
        calificacion = float(input(f"Ingrese la calificación {j + 1} para {nombreAlumno}: "))
        calificaciones.append(calificacion)
    
    # Diccionario con la información del alumno
    alumno = {
        'Alumno': nombreAlumno,
        'Notas': calificaciones
    }

    # Agregando el diccionario a la lista de alumnos
    listaAlumnos.append(alumno)

print("\nListado de Alumnos:")
for alumno in listaAlumnos:
    print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")

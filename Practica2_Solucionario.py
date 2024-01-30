##################### Problema 1 #####################

for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        print(num)


##################### Problema 2 #####################

n = 5 
# Parte superior del patrón
for i in range(1, n + 1):
    print('* ' * i)

# Parte inferior del patrón
for i in range(n - 1, 0, -1):
    print('* ' * i)


##################### Problema 3 #####################
    
lista = []
n=1
while n != 0:
    respuesta = input("Desea ingresar un numero?: ")
    if respuesta.lower() == 'si':
        numero = int(input("Ingrese un numero: "))
        lista.append(numero)
    elif respuesta.lower() == 'no':
        break

print(lista)
cantidadPares = 0
cantidadImpares = 0

for i in range(len(lista)):
    if lista[i] %2 == 0:
        cantidadPares+=1
    elif lista[i] %2 == 1:
        cantidadImpares+=1

print(f"Cantidad de pares: {cantidadPares}")
print(f"Cantidad de impares: {cantidadImpares}")


##################### Problema 4 #####################

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


##################### Problema 5 #####################

def cantidadRepetidos (num:int, dig:int):
    numCadena = str(num)

    # Contando la cantidad de veces que aparece el dígito en el número
    nroVeces = numCadena.count(str(dig))

    return nroVeces

numero = int(input("Ingrese un numero: "))
digito = int(input("Ingrese un digito: "))
             
nRepetidos = cantidadRepetidos(numero, digito)

print(f"Cantidad de veces {digito} en el numero {numero}: {nRepetidos}")


##################### Problema 6 #####################

def generarFibonacci(limite:int):
    a, b = 0, 1

    serie = [a]

    # Generando la serie de Fibonacci hasta el límite
    while b <= limite:
        serie.append(b)
        a, b = b, a + b

    return serie

limiteSuperior = 50

serieFibonacci = generarFibonacci(limiteSuperior)

print("Serie de Fibonacci hasta", limiteSuperior, ":", serieFibonacci)


##################### Problema 7 #####################

def verificarPrimo(num:int):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

numero = int(input("Ingrese un número: "))

if verificarPrimo(numero):
    print("Es un número primo.")
else:
    print("No es un número primo.")


##################### Problema 8 #####################
    
def calcularFactorial(num:int):
    if num == 0:
        return 1
    # Aplicando recursividad
    else:
        return num * calcularFactorial(num - 1)

while True:
    numero = int(input("Ingrese un número: "))

    if numero < 0:
        print("Por favor, ingrese un número entero no negativo.")
    else:
        break

resultadoFac = calcularFactorial(numero)
print(f"El factorial de {numero} es: {resultadoFac}")


##################### Problema 9 #####################

def omitirVocales(cadena:str):
    vocales = "aeiouAEIOU"
    resultado = ''.join(caracter for caracter in cadena if caracter not in vocales)
    return resultado

texto = input("Ingrese una cadena de texto: ")

resultado = omitirVocales(texto)
print("Texto con vocales omitidas:", resultado)


##################### Problema 10 #####################

def obtenerNumeroMes(mes):
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    return meses.index(mes) + 1

def formatearFecha(fecha):
    partes = fecha.split()
    
    if '/' in fecha:
        mes, dia, anio = map(int, fecha.split('/'))
    else:
        mes = obtenerNumeroMes(partes[0])
        dia = int(partes[1].strip(','))
        anio = int(partes[2])

    return f"{anio:04d}-{mes:02d}-{dia:02d}"

cadenaFecha = input("Ingrese una fecha (mes-día-año o mes día, año): ")

fechaFormateada = formatearFecha(cadenaFecha)
print("La fecha formateada es:", fechaFormateada)

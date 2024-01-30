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

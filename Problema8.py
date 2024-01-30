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

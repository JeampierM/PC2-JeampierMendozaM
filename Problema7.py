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

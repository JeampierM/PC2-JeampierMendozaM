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
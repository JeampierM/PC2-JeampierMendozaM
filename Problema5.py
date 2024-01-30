def cantidadRepetidos (num:int, dig:int):
    numCadena = str(num)

    # Contando la cantidad de veces que aparece el dígito en el número
    nroVeces = numCadena.count(str(dig))

    return nroVeces

numero = int(input("Ingrese un numero: "))
digito = int(input("Ingrese un digito: "))
             
nRepetidos = cantidadRepetidos(numero, digito)

print(f"Cantidad de veces {digito} en el numero {numero}: {nRepetidos}")
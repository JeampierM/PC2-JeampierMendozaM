def omitirVocales(cadena:str):
    vocales = "aeiouAEIOU"
    resultado = ''.join(caracter for caracter in cadena if caracter not in vocales)
    return resultado

texto = input("Ingrese una cadena de texto: ")

resultado = omitirVocales(texto)
print("Texto con vocales omitidas:", resultado)

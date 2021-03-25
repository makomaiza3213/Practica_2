texto = input('Ingrese un texto: ')

palabra = input("Ingrese la palabra que desea buscar :")

palabra = palabra.upper()

texto2 = texto.upper()

cant = texto2.count(palabra)

print(cant)
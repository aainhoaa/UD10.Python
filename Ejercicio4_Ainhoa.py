def juntar_listas(lista1, lista2, conector):
    resultado = []
    for palabra1, palabra2 in zip(lista1, lista2):
        resultado.append(palabra1 + conector + palabra2)
    return resultado
lista1 = []
print('En la lista 1 tiene que indicar 3 palabras.')
for i in range(1,4):
    pregunta = input(f"Introduzca su palabra numero {i}: ")
    lista1.append(pregunta)
lista2 = []
print('En la lista 2 tiene que indicar 3 palabras.')
for i in range(1,4):
    pregunta = input(f"Introduzca su palabra numero {1}: ")
    lista2.append(pregunta)
conector = "-"
print(f'Las palabras resultantes son: ', juntar_listas(lista1, lista2, conector))
def crear_lista():
    potencia = int(input("La lista de numeros es: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\nA que potencia los quiere elevar?\n"))
    lista = [x ** potencia for x in range(0, 11)]
    return lista
print(crear_lista())
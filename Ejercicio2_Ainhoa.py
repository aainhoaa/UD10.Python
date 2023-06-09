from functools import reduce
def numeros():
    lista_numeros = []
    for i in range(5):
        numero = int(input("Ingrese su numero entre 0 y 10: "))
        while numero<0 or numero>10:
            print("El numero no es valido, debe estar entre 0 y 10.")
            numero = int (input("Ingrese un numero valido: "))
        lista_numeros.append(numero)
        print(f'Los numeros de momento son: {lista_numeros}')
    numeros_str = list(map(str, lista_numeros))
    resultado = reduce(lambda x,y:x+y, numeros_str)
    print(f'La secuencia de numeros corresponde al numero: {resultado}')
numeros()
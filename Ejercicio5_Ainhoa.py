def lista_diccionario(lista):
    diccionario = {}
    for indice, valor in enumerate(lista):
        diccionario[valor] = indice
    return diccionario
lista = ["casa", "coche", "silla", "mesa"]
print ('La enumeracion del diccionario es: ',lista_diccionario(lista))
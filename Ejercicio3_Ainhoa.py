def palabra(lista, letra):
    filtro = list(filter(lambda palabra: palabra.startswith(letra),lista))
    return filtro
lista_palabras = ['agua', 'burro', 'casa', 'dedo', 'arbol', 'pepita', 'jabon', 'mesa', 'teclado', 'raton', 'barba', 'rueda', 'sabana', 'gato']
seleccion_palabra = input(f"Las palabras de la lista son: {lista_palabras}\nCual es su letra para filtrat?\n")
print(f'Las palabras que comienzan por "{seleccion_palabra}" son: ', palabra(lista_palabras, seleccion_palabra) )
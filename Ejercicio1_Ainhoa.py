def lenp(frase):
    frase = input("Introduzca la frase: ")
    return list(map(len, frase.split(" ")))
print(f"La longitud de cada palabra es: {lenp('')}")
def pares():
    lista = []
    comienzo = int(input("Introduzca el comienzo del tramo: "))
    final = int(input("Indique el final del tramo: "))
    contador = 0
    for i in range(comienzo,final):
        if i %2==0:
            if contador < 10:
                lista.append(i)
                contador += 1
            else:
                break
    return lista
print(pares())
n1 = float(input("Introduzca un digito (el numero que quiere dividir): "))
n2 = float(input("Introduzca otro digito (el numero por el cual lo dividiremos): "))
def dividir(n1, n2):
    try:
        result = n1/n2
    except ZeroDivisionError:
        print("Error, el dividendo (el que divide) es CERO!")
    else:
        print("El resultado de dividir {} y {} es {}".format(n1, n2, result))
dividir(n1,n2)
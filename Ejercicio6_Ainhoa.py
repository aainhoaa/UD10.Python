lista_num=[]


for i in range (0,7):
    pregunta=int(input(f"Introduzca su digito {i}: "))
    lista_num.append(pregunta)

repeticiones = {}

for i, num in enumerate(lista_num):
    if num in repeticiones:
        repeticiones[num][0] += 1
        repeticiones[num][1].append(i)
    else:
        repeticiones[num] = [1, [i]]

duplicados = {k:v for k,v in repeticiones.items() if v[0] > 1}

for k,v in duplicados.items():
    print(f"La lista de numeros es {lista_num}",f"\nEl numero {k} se repite {v[0]} veces en las posiciones {v[1]}")
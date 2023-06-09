try:
    with open("/home/cicles/AO", "r") as f:
        contenido =f.read()
except FileNotFoundError:
    print("Error al buscar fichero ojito.txt")
except IOError:
    print("Error de entrada y de salida")
else:
    print("Se puede trabajar!")
    print(contenido)
finally:
    if not(f.closed):
        f.close()
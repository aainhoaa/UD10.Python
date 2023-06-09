class Animal:
    def __init__(self, especie, edad):
        self.especie=especie
        self.edad=edad
    def hablar(self):
        pass
    def movimiento(self):
        pass
    def soy(self):
        print("Soy un animal del tipo {}".format(self.especie))


class Caballo(Animal):
    def hablar(self):
        print("El sonido que me caracteriza es: iiiiiii")
    def movimiento(self):
        print("Me muevo trotando!")


class Delfin(Animal):
    def hablar(self):
        print("El sonido que me caracteriza es: Txasss!")
    def movimiento(self):
        print("Me muevo nadando!")


class Abeja(Animal):
    def hablar(self):
        print("El sonido que me caracteriza es: Bzzzzz!")
    def movimiento(self):
        print("Me muevo volando!")
    def picar(self):
        print("Si me molestas, te picare")


class Humano(Animal):
    def __init__(self, especie, edad, nombre):
        super().__init__(especie,edad)
        self.nombre=nombre
    def hablar(self):
        print("El sonido que me caracteriza es la palabra Hola!")
    def movimiento(self):
        print("Me muevo caminando")
    def soy(self):
        print("Soy un humano y me dicen {}".format(self.nombre))


class Fiet(Humano):
    def __init__(self, especie, edad, nombre, padres):
        super().__init__(especie,edad,nombre)
        self.padres=padres
    def nombre_padres(self):
        print("Mi padre se llama {} y mi madre {}".format(self.padres[0],self.padres[1]))
   
class Centauro(Caballo, Humano):
    def soy(self):
        print("Soy un centauro y surjo de {}".format(Centauro.__mro__))
   
class Show:
    def soy(self):
        print("Patito, eso es lo que soy")
    def movimiento(self):
        print("Patito, asi es como me muevo")
    def hablar(self):
        print("Patito, asi es como hablo")


f= [Humano("Humano", 32, "Joan"), Caballo('mamifero', 10), Delfin('mamifero', 23), Abeja('insecto', 1), Fiet('humano', 6, 'Pau',('Joan', 'Luz')), Show(), Centauro('centauro', 40, 'quiron')]


nombres = []
for e in f:
    nombres.append(e.__class__.__name__)


print("¿Qué animal quieres?")
for i in range(len(nombres)):
    print("{} - {}".format(i+1, nombres[i]))
opcion = int(input("Ingresa el número del animal: "))


if opcion < 1 or opcion > len(nombres):
    print("Opción inválida")
else:
    animal = f[opcion-1]
   
    animal.soy()
    animal.movimiento()
    animal.hablar()
    print("Tengo {} años".format(animal.edad))
   
    if type(animal)==Fiet:
        animal.nombre_padres()
    if type(animal)==Abeja:
        animal.picar()

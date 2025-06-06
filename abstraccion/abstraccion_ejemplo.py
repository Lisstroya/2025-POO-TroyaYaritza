from abc import ABC,  abstractmethod
class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass
class Perro(Animal):
    def sonido(self):
        print("El perro hace: ¡Guauu!")

class Gato(Animal):
    def sonido(self):
        print("El gato dice: ¡Miauu!")

perro = Perro()
perro.sonido()

gato = Gato()
gato.sonido()

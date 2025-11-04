from abc import ABC, abstractmethod

# abstract class: es una clase que no puede ser instanciada, solo puede ser heredada
class Animal(ABC):

    # cantidad de animales, es un atributo estatico, se comparte entre todas las instancias de la clase
    cantidad_animales = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Animal.cantidad_animales += 1
    
    # decorador abstractmethod: es un decorador que Obliga si o si las clases hijas deben implementar este metodo
    @abstractmethod
    def sonido(self): # no colocar esta funcion en clases hijas da error (por el abstractmethod)
        pass

    # metodo de clase (classmethod): es un metodo que se puede ejecutar desde la clase misma
    # cls: se refiere a la clase (cantidad_animales es un atributo estatico de la clase Animal)
    @classmethod
    def obtener_cantidad_animales(cls):
        print(f"Cantidad de animales: {cls.cantidad_animales}")

# clase hijas
class Perro(Animal):
    def sonido(self):
        print(f"guau")

    def aullar(self):
        print(f"El perro {self.nombre} esta aullando")
        
    
class Gato(Animal):
    def sonido(self):
        print(f"miau")
    
    def maullar(self):
        print(f"El gato {self.nombre} esta maullando")

# ejemplo de uso
perro = Perro("Firulais")
gato = Gato("Michi")

perro.sonido()
gato.maullar()
Animal.obtener_cantidad_animales()


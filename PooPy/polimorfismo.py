# super clase 
class Instrumento():
    def __init__(self, nombre):
        self.nombre = nombre
        
    def tocar(self):
        print("Tocando el instrumentos musicales")

# sub clases

class Guitarra(Instrumento):
    # inicializamos el atributo nombre de la clase padre
    def __init__(self, nombre):
        super().__init__(nombre)

    def tocar(self):
        print("Tocando la guitarra")

class Piano(Instrumento):
    def __init__(self, nombre):
        super().__init__(nombre)

    def tocar(self):
        print("Tocando el piano")

class Bateria(Instrumento):
    def __init__(self, nombre):
        super().__init__(nombre)

    def tocar(self):
        print("Tocando la bateria")

# ejemplo de polimorfismo
guitarra = Guitarra("Guitarra") # pasamos el nombre de la guitarra
piano = Piano("Piano") # pasamos el nombre del piano
bateria = Bateria("Bateria") # pasamos el nombre de la bateria

# esto es polimorfismo, porque estamos llamando al metodo tocar de la clase Guitarra, Piano y Bateria
# pero cada una tiene su propia implementacion
guitarra.tocar()
piano.tocar()
bateria.tocar()

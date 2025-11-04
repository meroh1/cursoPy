'''
Herencia:
    - es el proceso de crear una nueva clase a partir de una clase existente
    - la nueva clase hereda los atributos y metodos de la clase existente
    - la nueva clase puede agregar nuevos atributos y metodos
    - la nueva clase puede modificar los atributos y metodos de la clase existente
'''

# clase padre
class Persona:
    def __init__(self, nombre, poder):
        self.nombre = nombre
        self.poder = poder

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo el poder de {self.poder}")
    
# clase hija    
class SuperHeroe(Persona):
    # con esta claseHija (SuperHeroe) vamos a agregar un nuevo atributo (nombreHeroe)
    def __init__(self, nombre, poder, nombreHeroe):
        # invocamos el constructor de la clase padre para inicializar los atributos de la clase padre
        # en la clase hija, en este caso, Persona en SuperHeroe
        super().__init__(nombre, poder)
        self.nombreHeroe = nombreHeroe # aumentamos el atributo nombreHeroe de la clase hija (SuperHeroe)

    def fraceHeroe(self):
        print(f"Soy el heroe {self.nombreHeroe} con el poder de {self.poder}")

class Villano(Persona):
    def fraceVillano(self):
        print(f"Soy el villano {self.nombre} con el poder de {self.poder}")


# ejemplo con instancia en clase padre

persona = Persona("Juan", "volar")
persona2 = Persona("Pedro", "rayoLaser")

# llamamos al metodo saludar de la clase Persona
#persona.saludar()
# llamamos al metodo fraceHeroe de la clase SuperHeroe
#SuperHeroe.fraceHeroe(persona)
# llamamos al metodo fraceVillano de la clase Villano
Villano.fraceVillano(persona2)

# ejemplo con instancia en clase hija, 

# name, poder son de la clase padre, nombreHeroe es de la clase hija
persona3 = SuperHeroe("Clark Kent", "teremoto", "mcklovin")
persona3.fraceHeroe()
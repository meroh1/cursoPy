# es la plantilla para la creacion de objetos
#class Robot:
#    name = "roboMero"

# Instancia: es la creacion de un objeto a partir de una clase llamada Robot
#robot1 = Robot()
#print(robot1.name) # imprime el nombre del robot

# ___________________________

class Robot:
    # constructor: es un metodo especial que se ejecuta al crear
    # una instancia de la clase
    # self: se refiere a la instancia especifica
    def __init__(self, name, tipo):
        self.name = name
        self.tipo = tipo

    # metodo: es una funcion que define el comportamiento de un objeto especifico
    def saludar(self):
        print(f"Hola, soy {self.name}")
    
    def saltar(self):
        if self.tipo == "industrial":
            print(f"Soy el robot {self.tipo}:{self.name} y estoy saltando")
        else:
            print(f"Soy el robot {self.tipo}:{self.name} y no puedo saltar")


# instancia: es la creacion de un objeto a partir de una clase (Robot)
robot1 = Robot("roboMero", "industrial")
robot2 = Robot("roboMerito", "domestico")

#print(robot1.name)
#print(robot1.tipo)
robot1.saludar()
robot1.saltar()
print("--------------------------------")
robot2.saludar()
robot2.saltar()
    

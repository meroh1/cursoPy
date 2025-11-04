'''
Sin encapsulamiento (no recomendado):
    - se puede acceder a los atributos de la clase directamente
'''
class CajaFuerte2:
    def __init__(self, clave, saldo):
        self.clave = clave
        self.saldo = saldo

caja2 = CajaFuerte2("1234", 1000)

print(caja2.clave)
print(caja2.saldo)

# hacer una cariable privad, nos tumba error si intentamos acceder a ella
#print(caja2.__clave) 
#print(caja2.__saldo)

print("--------------------------------")
'''
Encapsulamiento:
    - atributos protegidos: se definen con un guion bajo al inicio del nombre del atributo
    - atributos privados: se definen con dos guiones bajos al inicio del nombre del atributo

    - Getters: son metodos que se usan para obtener el valor de un atributo protegido o privado
    - Setters: son metodos que se usan para asignar un valor a un atributo protegido o privado
'''

# creamos la clase caja fuerte, la cual tiene una clave y un saldo
class CajaFuerte:
    # creamos el constructor de la cajaFuere, inicializamos los atributos de la clase
    def __init__(self, clave, saldo):
        # atributos privados
        self.__clave = clave
        self.__saldo = saldo

    # Getters: son metodos que se usan para obtener el valor de un atributo protegido o privado
    def get_clave(self):
        return self.__clave
    def get_saldo(self):
        return self.__saldo
    
    # Setters: son metodos que se usan para asignar un valor a un atributo protegido
    def set_clave(self, clave):
        self.__clave = clave
    def set_saldo(self, saldo):
        self.__saldo = saldo

# instanciamos la clase CajaFuerte
# y asignamos valores a los atributos
caja = CajaFuerte("1234", 1000)

# asignamos nuevos valores a los atributos
caja.set_clave("123")
caja.set_saldo(2000)

# obtenemos los nuevos valores de los atributos
print(caja.get_clave())
print(caja.get_saldo())

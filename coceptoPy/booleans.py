# tipo de dato que toma dos valores: True o False (verdadero o falso)

a = True
b = False

# nos ayuda a tomar decisiones en el codigo

# estructuras que devuelven true
string = bool("Hola")
numero = bool(15)
lista = bool([1, 2, 3])
diccionario = bool({"nombre": "Ana", "edad": 25})

print(string)        # True

# estructuras que devuelven false
string_vacio = bool("")
numero_cero = bool(0)
lista_vacia = bool([])
diccionario_vacio = bool({})
none = bool(None)

print(lista_vacia)  # False

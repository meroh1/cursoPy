# Condicionales en Python

# Ejemplo de condicional simple
edad = 18
if edad > 17:
    print("Eres mayor de edad")

# Ejemplo 2
var1 = 10
var2 = 20
if var1 > var2:
    print("var2 es mayor que var1")
elif var1 < var2:
    print("var1 es menor que var2")
else:
    print("var1 es igual a var2")

# Ejemplo de condicional compuesto Sin Anidar

# Si la edad es mayor a 12 y menor a 18
if edad > 12 and edad < 18:
    print("Eres una persona joven") # true: ejectuta esto
# Si el if anterior no se cumple, se evalúa esta condición 
elif edad >= 18 and edad <= 49:
    print("Eres una persona adulta") # true: ejectuta esto
# Si el elif anterior no se cumple, se evalúa esta condición
elif edad > 49 and edad <= 115:
    print("Eres una persona adulta mayor") # true: ejectuta esto
# Si ninguna de las condiciones anteriores se cumple, se ejecuta el else
else:
    print("Edad no válida") 

# Ejemplo de condicional Anidado

if edad >= 18 and edad <= 49:
    print("Eres una persona adulta")
    if edad >= 18 and edad <= 29:
        print("Eres un adulto joven")
    elif edad >= 30 and edad <= 39:
        print("Eres un adulto de mediana edad")
    else:
        print("Eres un adulto maduro")
else:
    print("No eres una persona adulta")



# Entrar a una discoteca, pero hay palcos permitidos dependiendo de la edad
# Dentro de cada palco, se dividen en 2 categorías de colores dependiendo de la edad

user1 = 41
# user1 esta en rango de entrar a palco lvl 1?
if user1 >= 18 and user1 <30:
    print("palco lvl 1")
    if user1 >= 18 and user1 <= 24:
        print("Color rojo")
    else:                          # elif user1 >= 25 and user1 < 30: no es necesario
        print("Color azul")
# user1 esta en rango de entrar a palco lvl 2?
elif user1 >= 30 and user1 < 50:    
    print("palco lvl 2")
    if user1 == 30:
        print("Color Verde bienvenida al palco lvl 2")
    elif user1 > 30 and user1 <= 40 and user1 != 35:
        print("Color Amarillo")
    else: #de lo contrario les pasaran un purpel, q pasa con 35, q color el dan
        print("Color Purpura")
else:
    print("No tienes acceso a ningun palco")

# Shorthands 

a = 5
b = 2

if a > b: print("a es mayor que b")  # condicional en una sola línea  # noqa: E701

print("a es mayor que b") if a > b else print("b es mayor o igual que a")  # operador ternario

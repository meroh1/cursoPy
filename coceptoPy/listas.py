#colecion (arrays) que permite almacenar elementos en una sola Variable
#son ordenadas y mutables, es decir tienen un indice y se pueden modificar

# indice       0          1          2          3
mi_lista = ["manzana", "banana", "cereza", "naranja"]

varLen = len(mi_lista)  #len() devuelve la cantidad de elementos en la lista
print("Cantidad de elementos en la lista:", varLen)

# Acceder a elementos de la lista

# print("Primer elemento:", mi_lista[0])
# print("Segundo elemento:", mi_lista[1:3])  # Accede a elementos desde el índice 1 hasta el 2
# print("Último elemento:", mi_lista[:2])  # hasta el  no incluido
# print("Último elemento:", mi_lista[-1])  # Accede al último elemento usando índice negativo

# -- Listas de diferentes tipos de datos

listStrings = ["Hola", "Mundo", "Python"]
listNumbers = [10, 20, 30, 40, 50]
listMixed = ["Texto", 100, 3.14, True]

print("Lista de cadenas:", listStrings)
print("Lista de números:", listNumbers)
print("Lista mixta:", listMixed)

listConstruida = list(("Rojo", 2, False))  # Si listMixed fuera tupla, usaríamos list()
print("Lista construida con list():", listConstruida)


# verificar si existe un elemento en la lista
if "manzana" in mi_lista:
    print("La manzana está en la lista.")


# Modificar elementos de la lista

# indice            0             1          2            3        4   
listMaterias = ["Matemáticas", "Historia", "Ciencias", "Arte", "ed.Física"]

listMaterias[1] = "Geografía"  # Cambia "Historia" por "Geografía"
listMaterias[2:4] = ["Religión", "políticas"]  # Cambia "Ciencias" y "Arte" por "Religión" y "políticas"
print("Lista de materias modificada:", listMaterias)

# Agregar elementos a la lista
#listMaterias.insert(2, "Música")  # Inserta "Música" en el índice 2
#listMaterias.append("Inglés")  # Agrega "Inglés" al final de la lista
#print("Lista después de agregar elementos:", listMaterias)

# agregar una lista a otra lista
# extend() permite agregar colecciones a una lista 
#listNewMaterias = ["Biología", "Química"]
#listMaterias.extend(listNewMaterias)  # Agrega los elementos de listNewMaterias
#print("Lista x lista:", listMaterias)

#Eliminar elementos de la lista
listMaterias.remove("políticas")  # Elimina "políticas" de la lista
listMaterias.pop()  # Elimina el último elemento de la lista
listMaterias.pop(1)  # Elimina el elemento en el índice 1
del listMaterias[1]  # Elimina el elemento usando del en el índice 1

#limpiar toda la lista
listLimpia = ["carro", "moto", "bicicleta", "avion"]
listLimpia.clear()  # Elimina todos los elementos de la lista


# Recorrer una lista
listLenguajes = ["Python", "Java", "C++", "JavaScript", "Ruby", "Go", "Swift", "Kotlin"]
for lenguaje in listLenguajes:
    #print("Lenguaje:", lenguaje)
    break

# forrma de saber el indice de cada elemento de una lista
for i in range(len(listLenguajes)):
    print( i,". ", listLenguajes[i])


#ejemplo de uso: los array de la lista q tengan la letra 'o'
listArraysO = []

for array in listLenguajes:

    if 'o' in array:
        listArraysO.append(array)
        print("arrayO:", array)


#ordenar una lista
listNumeros = [5, 2, 9, 1, 5, 6]
listNumeros.sort()  # Ordena la lista en orden ascendente
print("Lista ordenada:", listNumeros)

listNumeros.sort(reverse=True)  # Ordena la lista en orden descendente
print("ordenada descendente:", listNumeros)

listNumeros.reverse()  # Invierte el orden de los elementos en la lista
print("revertida:", listNumeros)

# Crea una copia de la lista meses
meses = ["enero", "febrero", "marzo", "abril"]
meses2 = ['mayo', 'junio', 'julio', 'agosto']
copyMeses = meses.copy() 
copyMeses2 = list(meses2)

print("Copia de meses:", copyMeses)
print("Copia de meses2:", copyMeses2)
# unir dos listas
listaUnida = meses + meses2
#meses.extend(meses2)  # otra forma de unir dos listas
print("Lista unida:", listaUnida)
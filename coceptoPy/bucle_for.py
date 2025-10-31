# estructura que repite un bloque de codigo un numero determinado de veces

listElementos = ['agua', 'fuego', 'tierra', 'aire', 'plasma']

#recorrer la lista
for elemento in listElementos:
    print("Elemento:", elemento)

    # condicion de ruptura
    if elemento == 'tierra':
        print("¡Esos son todos los elementos!")
        # break
        continue

# recorrer una cadena de caracteres
txtNew =  'un texto largo'

for caracter in txtNew:
    print("Caracter:", caracter)

print("-----")

# recorrer un rango de numeros
for numero in range(5): # 0,1,2,3,4
    print("Numero:", numero)

print("-----")

# rango con inicio y fin
for numero in range(2, 7): # 2,3,4,5,6
    print("Numero en rango:", numero)

print("-----")

 # rango con paso
for numero in range(1, 10, 2):  # 1,3,5,7,9
    print("cada 2:", numero)

# ciclo anidado
letras = ['a', 'b', 'c']
numeros = [1, 2, 3]
for letra in letras:
    for numero in numeros:
        print("Combinacion:", letra, numero)
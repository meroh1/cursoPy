varText = 'Practica de cadenas de exto con Python'
print(varText)

varInt = 1
print(type(varInt))

varFloat = 3.1416
print(type(varFloat))

varComplex = 5 + 3j
print(type(varComplex))

varList = [0,1,2,3,4,5,6,7,8,9]
print(type(varList))

varTuple = ('manzana', 'banana', 'cereza')
print(type(varTuple))
print(varTuple[0])  # Output: banana


varRango = range(1, 10, 2)
print(type(varRango))
for z in varRango:
    print(z, end=' ')  # Output: 1 2 3 4 5 6 7 8 9

diccionario = {
    'name': 'mero',
    'type': 'fish',
    'diccionary': {
        'key1': 'mero interno',
        'key2': 'mero pescao'
    },
}
print('\nkey1: ' + diccionario['name'])  # Output: mero
print('key2: ' + diccionario['diccionary']['key2'])  # Output: mero pescao

varSet = {1,2,2,3,2,3,4,3,6,2,1,7}
print(type(varSet))
print(varSet)  # Output: {1, 2, 3, 4, 6, 7}

varFrozenSet = frozenset([ 1,2,3,2,3,3])
print(type(varFrozenSet))
print(varFrozenSet)  # Output: frozenset({1, 2, 3})

varBoolean1 = True
varBoolean2 = False
print(type(varBoolean1))


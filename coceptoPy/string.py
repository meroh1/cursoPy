from calendar import c


varText = '- Practica de cadenas de texto con Python'
varText2 = "- Otra cadena de texto"
varText3 = '''- Cadena de texto
multilinea'''

print(varText)
print(type(varText))

#--- acceso a caracteres individuales ---

caracter = varText[6]
print(caracter)

#--- longitud de la cadena ---
# len -> length (longitud)

longitud = len(varText)
print(longitud)


# in / not in 
cadenaBuscar = 'Python'
resultado = cadenaBuscar in varText # 'Python' esta en varText?
print(resultado)

resultado2 = 'Java' not in varText # 'Java' No esta en varText?
print(resultado2)

#slice
print(varText[0:8])  # desde el caracter 0 hasta el 7
print(varText[10:])  # desde el caracter 10 hasta el final
print(varText[:10])  # desde el inicio hasta el caracter 9
print(varText[-6:])  # desde el caracter -6 hasta el final

# modificacion de cadenas

txtEspacios = '   Hola Mundo   '
txtComas = "Jelou gente de yutu"

varMayus = varText.upper()
print(varMayus)

varMinus = varText.lower()
print(varMinus)

varSinEspacios = txtEspacios.strip()
print(varSinEspacios)
print('count: ' + str(len(varSinEspacios)))

varTextModificada = varText.replace('Python', 'JavaScript')
print(varTextModificada)

varSeparar = txtComas.split(",") # se puede usar tmb /
print(varSeparar)  # Output: ['Jelou', ' gente', ' de', ' yutu', ' :D']

txtBackSlash = 'Juaan un dia me dijo \'almorzamos?\' y yo le dije \"claro que si\"' 
# "juan "ola" maria " MAL
print(txtBackSlash)

#varUrl = 'D:\zzudb_black\usb_black\NitroPro14' # mala practica, puede generar errores
varUrl = 'D:\\zzudb_black\\usb_black\\NitroPro14'
print(varUrl)

varN = 'salto de..\n. linea'
print(varN)

# concatenacion
a = 'jelou'
b = 'word'
c = a + ' - ' + b  # noqa: F811
print(c)  # Output: jelou - word

#f-strings (template strings) variables dentro de una string
d = 'pedro'
e = 23
#f = d + e # error no se puede concatenar str con int

f = a + d # string + string
print(f)  # Output: jeloupedro

#-- Usando f-strings
name = 'Danne'
age = 25
greeting = f'Mi nombre es {name} y tengo {age} años.'
print(greeting)  # Output: Mi nombre es Danne y tengo 25 años.

varPrueba = f'La multiplicacion de 5 x 3 es {5 * 3}'
print(varPrueba)  # podemos colocar expresiones dentro de {}

#--- formato avanzado con f-strings ---
precio = 49.99      
impuesto = 0.07
total = precio * (1 + impuesto)
mensaje = f'El precio total es: ${total:.2f}'  # Formateo a 2 decimales
print(mensaje)  # Output: El precio total es: $53.49


#------ Metodos de cadena comunes ------
varZzz = '''Esto es una CADENA de texto
que ABARCA varias LINEAS.'''

varCapitalize = varZzz.capitalize() # Primera letra mayus, resto minus
print(varCapitalize)

varTitle = varZzz.title() # Primera letra de cada palabra en mayus
print(varTitle)

varStart = varZzz.startswith('esto') # Comienza con 'Esto'?
print(varStart)

varEnd = varZzz.endswith('LINEAS.') # Termina con 'LINEAS.'?
print(varEnd)

varFind = varZzz.find('varias') # posicion del caracter inicial de 'varias'
print(varFind)

varFind2 = varZzz.find('python') # si no lo encuentra devuelve -1
print(varFind2)

varCount = varZzz.count('e') # cuantas veces aparece 'de'
print(varCount)
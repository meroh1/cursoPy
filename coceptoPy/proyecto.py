print('jelou word')

if 5>3:
    print('cinco es mayor que tres')
    if 5>4:
        print('cinco es mayor que cuatro')

#-------- separador --------
x = 5   
txt = "esto es texto"   

print('x: ',x)    
print('txt: ',txt)


num1 = "7"  
num2 = 2   
num2 = 4 # reasignacion de valor de la variable num2 
Num2 = 3 # caseSensitive (interperta mayus y minus, como variables diferentes)

  
print('num1: ', num1)      
print('num2: ', num2)   
print('Num2: ', Num2)

#print("ejemplo suma: ", int(num1) + num2) 

#-------- separador --------

#  forma de solucionarlo

varGlobal = 'txt global fuera'

def funcionZzz ():
    global varScope #usamos funcion global en la variable varScope
    
    varGlobal = 'txt global en funcionZzz'
    varScope = 'txt scope en funcionZzz'
    print(varGlobal) #solo disponible en este scope 
    print(varScope)

funcionZzz()

print(varGlobal)
print(varScope) # deberia dar error SI no se usa global en la funcion


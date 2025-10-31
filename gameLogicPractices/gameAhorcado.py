import random

def palabraAleatoria():
    listaPalabras = ["python", "java", "javascript", "html", "css"]

    #choice -> elige una palabra aleatoria de la lista
    varPalabra = str(random.choice(listaPalabras))  #str -> convierte la palabra en una cadena de texto
    

    return varPalabra

def juegoAhorcado():
    varPalabra = palabraAleatoria()
    varPista = "* " * len(varPalabra)
    listPalabra = list(varPalabra)

    varIntentos = 1
    varMaxIntentos = 5

    print(f'''Bienvenido al juego de ahorcado\n
    Pistas de la palabra:\n
        - lenguajes de programacion\n
        - longitud: {varPista}\n   
        ''')
    
    while varIntentos < varMaxIntentos:

        print('-'*10)
        print(f"Intento: {varIntentos}/{varMaxIntentos}")
        varUser = input("Ingrese una letra/palabra: ").strip().lower()
        
        if varUser == varPalabra:
            print("Adivinaste la palabra")
            break
        elif varUser in listPalabra:
            print("Letra encontrada")
            varIntentos += 1
        else:
            print("Incorrecto")
            varIntentos += 1

    print(f"La palabra es: {varPalabra}")

juegoAhorcado()

    
    




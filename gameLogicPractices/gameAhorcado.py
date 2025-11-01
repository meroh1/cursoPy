# analizar como funciona y mejorar el codigo
import random

def funcionPalabraRandom():
    listPalabra = ["mario", "carlos", "felipe", "jeca"]
    return random.choice(listPalabra)

def funcionProgreso(listAcertadas, varPalabra):
    varProgreso = ""

    for letra in varPalabra:
        if letra in listAcertadas:
            varProgreso += letra
        else:
            varProgreso += "_"
    print(f'Pistas: {varProgreso}')
    return varProgreso

def ahorcado():
    print("--------------------------------")
    print("Bienvenido al juego del ahorcado")
    print("Adivina la palabra, con tematica de nombres comunes")
    
    varIntentos = 1
    varMaxIntentos = 11
    listAcertadas = []

    listPalabra = str(funcionPalabraRandom())
    varProgress = str(funcionProgreso(listAcertadas, listPalabra))

    while varProgress != listPalabra and varIntentos < varMaxIntentos:
        print("--------------------------------")
        print(f"Intento {varIntentos} de {varMaxIntentos-1}\n")
        varInput = input("Ingresa una letra: ")

        if varInput.isalpha() and len(varInput) == 1:
            if varInput in listPalabra:
                listAcertadas.append(varInput)
                
                print("Letra correcta")
                varProgress = str(funcionProgreso(listAcertadas, listPalabra))
            else:
                print("Letra incorrecta")
        else:
            print("Ingresa una letra valida")
        
        varIntentos += 1
    
    print("--------------------------------")
    print("Fin del juego")
    print(f"La palabra era: {listPalabra}")

ahorcado()

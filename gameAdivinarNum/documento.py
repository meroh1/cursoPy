import random

def funcion_principal():
    varRandom = random.randint(1, 100)
    varIntentos = 0
    varMaxIntentos = 10
    varAdivinado = False

    print("--------------------------------")
    print("Adivina el numero entre 1 y 100")
    print(f"Tienes {varMaxIntentos} intentos")
    while True:
        varIntentos += 1

        print("--------------------------------")   
        print(f"Intento: {varIntentos}/{varMaxIntentos}")
        
        if varIntentos > varMaxIntentos:
            print("Has agotado tus intentos")
            print(f"El numero era: {varRandom}")
            break

        varNum = int(input("adivina el numero: "))

        if varNum == varRandom:
            print("Adivinaste el numero")
            break
        elif varNum < varRandom:
            varRes = varRandom - varNum
            if varRes < 5:
                print("Estas muy caliente")
            elif varRes < 10:
                print("Estas caliente")
            elif varRes < 15:
                print("Estas tibio")
            elif varRes < 20:
                print("Estas frio")
            else:
                print("Estas muy frio")
        elif varNum > varRandom:
            varRes = varNum - varRandom
            if varRes < 5:
                print("Estas muy caliente")
            elif varRes < 10:
                print("Estas caliente")
            elif varRes < 15:
                print("Estas tibio")
            elif varRes < 20:
                print("Estas frio")
            else:
                print("Estas muy frio")

funcion_principal()
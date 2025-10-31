# estructura de un bucle while en Python

varCount = 0

while varCount < 12: # una while activo = True
    
    varCount += 1

    if varCount == 7:
        print(f"se salta el ciclo - {varCount}")
        continue # saltar a la siguiente iteracion del ciclo

    if varCount == 9:
        print(f"finaliza en el ciclo - {varCount}")
        break # salir del ciclo
    
    print("Ciclo numero:", varCount)
else:
    print(f"se completa el ciclo - {varCount}")


# While con Input del usuario

# la base para futuros ejercicios
while True:
    print("Escribe 'salir' para terminar el ciclo:")
    userInput = input("-> ").strip().lower()
    if userInput == "salir":
        break

# obtener 2 numeros, a traves de 2 inputs
# que operacion se va a realizar (+ ,  - ,  *, ** ,  / , //)
# despues de seleccionar la operacion, mostrar el resultado



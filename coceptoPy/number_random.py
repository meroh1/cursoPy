varEntero = 11
varFlotante = 13.12345678901234567890
varComplex = 5 + 2j

integerFloat = float(varEntero) # 11 a 11.0
floatInteger = int(varFlotante) # no aproxima
#--
integerComplex = complex(varEntero)
floatComplex = complex(varFlotante)

print(integerFloat)
print(floatInteger) 
print(integerComplex)
print(floatComplex)

# Random numbers
import random  # noqa: E402

# Genera un numero aleatorio entre 1 y 9
varRandom = random.randrange(1, 10) # stop no es incluido (10)
varPar = random.randrange(2, 11, 2) # numero par entre 2 y 11
varImpar = random.randrange(1, 11, 2) # numero impar entre 1 y 11


print(varRandom)
print(varPar)
print(varImpar)

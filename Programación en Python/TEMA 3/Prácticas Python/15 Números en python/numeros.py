'''Números de Python'''
edad = "34"  # edad entero i integer
print(edad)
nota = 8.9  # nota decimal o float
print(nota)

complejo = 5+3j
print(complejo)

sumando1 = 7
sumando2 = 3
suma = sumando1+sumando2
print("La suma de", sumando1, "+", sumando2, "es:", suma)

minuendo = 70
sustraendo = 30
resta = minuendo-sustraendo
print("La resta de", minuendo, "-", sustraendo, "es:", resta)

factor1 = 5
factor2 = 15
producto = factor1*factor2
print("El prodcuto de", factor1, "*", factor2, "es:", producto)

dividendo = 80
divisor = 3
division = dividendo/divisor
print("La division de", dividendo, "/", divisor, "es:", division)


# Division entera, muestra la parte entera de la division dividendo>divisor
dividendo = 7
divisor = 3
division_entera = dividendo//divisor
print("La division entera de", dividendo,
      "entre", divisor, "es:", division_entera)

# Division entera, muestra la parte entera de la division dividendo<divisor
dividendo = 3
divisor = 7
division_entera = dividendo//divisor
print("La division entera de", dividendo,
      "entre", divisor, "es:", division_entera)

# Resto o modulo, muestra el resto de la division sin  sacar decimales diviendo>divisor
dividendo = 7
divisor = 3
modulo = dividendo % divisor
print("La resto de la división entera sin sacar decimales es", dividendo,
      "modulo", divisor, "es:", modulo)

# Resto o modulo, muestra el resto de la division sin  sacar decimales diviendo<divisor
dividendo = 3
divisor = 7
modulo = dividendo % divisor
print("La resto de la división entera sin sacar decimales es", dividendo,
      "modulo", divisor, "es:", modulo)

# Potencias

base = 2
exponente = 3
potencia = base**exponente
print("La potencia de", base, "elevado", exponente, "es:", potencia)

# Algunos atajos en operaciones, forma larga

print("contador, aumento de 1")
contador = 8
print(contador)
contador = contador+1
print(contador)


print("Forma corta de operación, del contador anterior")
contador = 8
print(contador)
contador += 1
print(contador)


# Tambien vale para el resto de operaciones:
print("Forma corta con suma")
# Suma
a = 14
print(a)
a += 2
print(a)

print("Forma corta con resta")
a = 14
print(a)
a -= 2
print(a)

print("Forma corta con el producto")
a = 14
print(a)
a *= 2
print(a)


print("Forma corta con la división")
a = 14
print(a)
a /= 2
print(a)


print("Forma corta con la potencia")
a = 14
print(a)
a **= 2
print(a)

print("Forma corta con la división entera")
a = 25
print(a)
a //= 2
print(a)


print("Forma corta con módulo")
a = 25
print(a)
a %= 2
print(a)


a = 14
a += 2
a -= 2
a *= 2
a /= 2
a **= 2
a //= 2
a %= 2
print(a)

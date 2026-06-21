'''Módulo Math nativo'''
# Veámos algunas funciones nativas en python
# Round(arumento1, digito) redondeo.
# Hay que tener en cuenta que usa el redondeo bancario: redondeo al número PAR más proximo cuando es algo,5

# La parte entera es impar
print("Parte entera impar")

precio = 1.95
print(precio)
print("El precio redondeado es:", round(precio))

precio = 1.35
print(precio)
print("El precio redondeado es:", round(precio))

precio = 1.5
print(precio)
print("El precio redondeado es:", round(precio))

# Cambiando la parte entera a PAR
print("Parte entera es Par")

precio = 14.95
print(precio)
print("El precio redondeado es:", round(precio))

precio = 14.35
print(precio)
print("El precio redondeado es:", round(precio))

precio = 14.5
print(precio)
print("El precio redondeado es:", round(precio))

print(round(3.14159))

# Round(argumento,digitos)
print(round(3.14159, 1))
print(round(3.14159, 2))
print(round(3.14159, 3))
print(round(3.14159, 4))
print(round(3.14159, 5))


print(round(3.14159, -1))

print(round(4458.1242, -1))

print(round(1876.985, -1))
print(round(1876.985, -2))
print(round(1876.985, -3))

print(round(1876.985, 2))
print(round(1876.985, 1))

# Valor absoluto: coge el valor del numero sin signo.

print(abs(-98))
print(abs(104))
print(abs(+104))

a = -7
print(a)
a = abs(a)
print(a)



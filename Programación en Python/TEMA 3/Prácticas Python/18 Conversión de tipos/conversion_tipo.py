'''Conversion Tipos'''
# type(variable) dice de que tipo es la variable
print("**********int() 1**********")
numero1 = 9
print(type(numero1))

numero2 = 1
print(type(numero2))

numero3 = numero1+numero2
print(type(numero3))

print("**********fin int() 1**********")
# Error (esto tenemos que evitarlo)
# numero1 = "9"
# print(type(numero1))

# numero2 = 1
# print(type(numero2))

# numero3 = numero1+numero2
# print(type(numero3))
# print(numero3)

print("**********int() 2**********")
numero1 = "9"
print(type(numero1))

numero2 = 1
print(type(numero2))

numero3 = int(numero1)+numero2
print(type(numero3))
print(numero3)

print("**********int() 2**********")

print("**********int() 3**********")
numero1 = 17.9999
print(type(numero1))
print(numero1)

numero2 = int(numero1)
print(type(numero2))
print(numero2)

print("**********int() 2**********")

print("**********float()**********")
numero1 = 124
print(type(numero1))
print(numero1)

numero2 = float(numero1)
print(type(numero2))
print(numero2)

print("**********fin float()**********")

print("**********varios tipos compatible**********")
numero1 = 57
numero2 = 57.8
print(type(numero1))
print(type(numero2))

numero3 = numero1+numero2
print(type(numero3))
print(numero1)
print(numero2)
print(numero3)

print("**********fin varios tipos compatible**********")

print("**********str()**********")
a = 392
b = 2526
c = 12
print(str(a)+str(b)+str(c))

print("**********fin str()**********")

# bool() convierte a booleano, esto es especial
# Datos Falsy (se evaluarán como false) son:
#    string vacio "" Nada entrecomillas
#    0
#    objeto None
# Datos Truthy (se evaluarán como true) son:
#         string con algo dentro
print("**********bool()**********")
# Datos Falsy
print(bool(""))
print(bool(0))
print(bool(None))
# Datos Truthy
print(bool(" "))
print(bool("0"))
print("********** fin bool()**********")

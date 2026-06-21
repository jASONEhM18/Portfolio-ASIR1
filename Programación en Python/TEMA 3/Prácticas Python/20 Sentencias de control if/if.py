'''Sentencias if o condicionales'''
edad = 14
print(edad)
if edad >= 18:
    print("Puedes ver la película 1")
print("FIN 1")

#############################

edad = 14
print(edad)
if edad >= 18:
    print("Puedes ver la película 2")
print("FIN 2")

#############################

edad = 14
print(edad)
if edad >= 18:
    print("Puedes ver la película 3")

else:
    print("No puedes entrar 3")


print("FIN 3")

#############################

edad = 20
print(edad)
if edad >= 18:
    print("Puedes ver la película 4")
else:
    print("No puedes entrar 4")
    print("Aqui no la puedes ver")

print("FIN 4")

#############################

edad = 14
print(edad)
if edad >= 18:
    print("Puedes ver la película 5")
else:
    print("No puedes entrar 5")
    print("Aqui no la puedes ver 5")

print("FIN 5")

#############################
# Incoherencia
edad = 20
print(edad)
if edad >= 18:
    print("Puedes ver la película 6")
else:
    print("No puedes entrar 6")

print("Aqui no la puedes ver 6")  # Error en la sangría

print("FIN 6")

#############################

edad = 20
print(edad)
if edad >= 18:
    print("Puedes ver la película 7, no tienes descuento")
else:
    print("No puedes entrar 7")
    print("Aqui no la puedes ver 7")

print("FIN 7")

#############################

edad = 66
print(edad)
if edad > 65:
    print("Puedes ver la película 8, con un descuento")
elif edad >= 18:
    print("Puedes ver la película, no tienes descuento")
else:
    print("No puedes entrar 8")
    print("Aquí no a puedes ver")

print("FIN 8")

################################

edad = 14
print(edad)
if edad > 65:
    print("Puedes ver la película 9, con un descuento")
elif edad >= 18:
    print("Puedes ver la película, no tienes descuento")
else:
    print("No puedes entrar 9")
    print("Aquí no a puedes ver")

print("FIN 9")

################################

edad = 67
print(edad)
if edad > 65:
    print("Puedes ver la película 10, con un descuento")
elif edad >= 18:
    print("Puedes ver la película, no tienes descuento")
else:
    print("No puedes entrar 10")
    print("Aquí no a puedes ver")

print("FIN 10")

################################
# ERROR
edad = 67
print(edad)
if edad >= 18:
    print("Puedes ver la película 11, no tienes descuento")
elif edad > 65:
    print("Puedes ver la película, con un descuento")
else:
    print("No puedes entrar 11")
    print("Aquí no a puedes ver")

print("FIN 11")
################################

edad = 70
print(edad)

if edad >= 70:
    print("Puedes ver la película 12 es gratis")
elif edad >= 65:
    print("Puedes ver la película, con un descuento")
elif edad >= 18:
    print("Puedes ver la película 12, no tienes descuento")
else:
    print("No puedes entrar 12")
    print("Aquí no la puedes ver")

print("FIN 12")

'''Métodos de string'''
# Los métodos son como una función que se encuentram dentro de un objeto.
asignatura = "Física Cuántica"
print(asignatura.upper())
print(asignatura.lower())

ciencia = "física del estado sólido"
print(ciencia.capitalize())

# Esto en css es capitalize.
print(ciencia.title())


ubicacion1 = " lagos de Covadonga   asturias"
print(ubicacion1.upper())
print(ubicacion1.lower())
print(ubicacion1.capitalize())
print(ubicacion1.title())

ubicacion2 = " cordillera del Himalaya   nepal   "
print(ubicacion2.strip())  # Elimina los espacios de delante y del final
print(ubicacion2.strip().capitalize())
print(ubicacion2.strip().title())

ubicacion3 = "   Sierra de Gredos     "
# Con lstrip quitas los espacio de la izquierda (left)
print(ubicacion3.lstrip())
print(ubicacion3.rstrip())  # Lo mismo pero a la derecha
print(ubicacion3.lstrip()+"Almanzor")
print(ubicacion3.rstrip()+"Almanzor")

# Existe otro método que lo que hace es encontrar una cadena de caracteres dentro de nuestro string y devolvernos el índice donde comienza.
# Hay que recordar que el índice empieza en 0
print(ubicacion3.find("S"))
# Es senstive case (sensible a mayúsculas)
print(ubicacion3.find("s"))
print(ubicacion3.find("Sierra"))  # Te dice donde empieza la palabra
print(ubicacion3.find("sierra"))  # Cuando no encuentra el valor da un -1
print(ubicacion3.find("Gr"))
print(ubicacion3.lstrip().find("S"))
print(ubicacion3.find("Física"))

# Reemplazar
# Si no lo encuentra no hace nada
print(ubicacion3.replace("gredos", "Guadarrama"))
print(ubicacion3.replace("Gredos", "Guadarrama"))
print(ubicacion3)
# ubicacion3 = ubicacion3.replace("Gredos", "Guadarrama")
# print(ubicacion3)

ubicacion3_guion = ubicacion3.strip().replace(" ", "_")
print(ubicacion3_guion)

ubicacion3_sin = ubicacion3.replace(" ", "")
print(ubicacion3_sin)


A = "Gredos"
B = "Guadarrama"
print(ubicacion3.replace(A, B))
print(ubicacion3)

print("de" in ubicacion3)
# Es sensistive case
print("De" in ubicacion3)

A = "de"
print(A in ubicacion3)

print("Cuántica" not in ubicacion3)
print("de" not in ubicacion3)

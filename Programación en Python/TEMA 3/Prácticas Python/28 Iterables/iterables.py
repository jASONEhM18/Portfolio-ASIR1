'''Iterables con Loop for'''
# Iterable
# range(número), strings, las listas (arrays unidimensionales), las tuplas (arrays multidimensionales)
# Las listas y tuplas las veremos mas adelante

for n in "Administración de Sistemas Informaticos en Red":
    print(n)

for caracter in "Administración de Sistemas Informaticos en Red":
    print(caracter)

with open("iterables.txt", "a") as fichero:
    for caracter in "Programación con Python":
        fichero.write(f'{caracter}\n')


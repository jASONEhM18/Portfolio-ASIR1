'''Escribir en archivo'''

# modo 'a' (Append): Añade la linea al final del archivo sin borrar lo que ya estaba escrito.

with open("append.txt", "a") as fichero:
    print("a")
    fichero.write("Hola, este es un texto de prueba.\n")
    print("a")
    fichero.write("Hola, este es un texto de prueba.\n")

# modo 'w' (Write): Crea el archivo si no existe o lo sobreescribe si ya existe (borra todo su contenido anterior).

dia="Jueves"
with open("escribe.txt", "w") as fichero:
    print("b")
    fichero.write(f'La variable {dia}\n')
    print("b")
    fichero.write("segunda.\n")

'''match case estructura'''
# Ejemplo de match-case (Python 3.10+)
while True:
    try:
        nota = input("Introduce la nota:")
        nota = float(nota)
        break
    except ValueError:
        print("Introduce un valor númerico, por favor")


# nota = float(input("Introduce la nota:")) producia un error
print(nota)
mensaje = "nada"
match nota:
    case n if n > 10:
        mensaje = "Nota fuera de rango"
    case n if n == 10:
        mensaje = "MH"
    case n if n >= 9:
        mensaje = "Sobresaliente"
    case n if n >= 7:
        mensaje = "Notable"
    case n if n >= 6:
        mensaje = "Bien"
    case n if n >= 5:
        mensaje = "Aprobado"
    case n if n >= 0:
        mensaje = "Suspenso"
    case n if n < 0:
        mensaje = "No es una nota"  # para números negativos

print(mensaje)

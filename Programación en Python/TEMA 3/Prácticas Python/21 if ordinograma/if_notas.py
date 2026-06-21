'''Ejercicio_notas'''
nota = float(input("Introduce la nota:"))
print(nota)
mensaje = "nada"
if nota > 10:
    mensaje = "Nota fuerda de rango"
elif nota == 10:
    mensaje = "MH"
elif nota >= 9:
    mensaje = "Sobresaliente"
elif nota >= 7:
    mensaje = "Notable"
elif nota >= 6:
    mensaje = "Bien"
elif nota >= 5:
    mensaje = "Aprobado"
elif nota >= 0:
    mensaje = "Suspenso"
else:
    mensaje = "No es una nota"  # para numeros negativos
print(mensaje)

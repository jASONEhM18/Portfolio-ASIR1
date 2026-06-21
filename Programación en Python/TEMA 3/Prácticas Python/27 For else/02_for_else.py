'''Más de bucles o Loop for'''

# contraseña = '1234'

# for n in range(3):
#     print("Intento:", n+1)
#     tucontraseña = input("introduce la constraseña a ver si aciertas: ")
#     if tucontraseña == contraseña:
#         print("Has acertado: ", contraseña, "en el intento", n+1)
#         break
# else:
#     print("No has acertado, has agotado todos los intentos")


usuario = 'jasonehm'
contraseña = 'jazonp.zc18'

for n in range(3):
    print("Intento:", n+1)
    tuusuario = input("Introduce tu Usuario: ")
    tucontraseña = input("Introduce tu contraseña: ")
    if tuusuario == usuario and tucontraseña == contraseña:
        print("Has acertado: ", usuario, contraseña, "en el intento", n+1)
        break
else:
    print("No has acertado, has agotado todos los intentos")

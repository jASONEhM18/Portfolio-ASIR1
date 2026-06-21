'''Operador ternario 01'''

edad = 15
print(edad)
if edad >= 18:
    mensaje = "Mayor de edad con if clasico"
else:
    mensaje = "Es Menor de edad con if clasico"

print(mensaje)

# Con el operador ternario se aumenta la eficacia del código
# Se llama ternario porque tiene 3 partes

edad = int(input("Introduce la edad:"))

mensaje = "Mayor de edad con if ternario" if edad >= 18 else "Es Menor de edad con if clasico"

print(mensaje)

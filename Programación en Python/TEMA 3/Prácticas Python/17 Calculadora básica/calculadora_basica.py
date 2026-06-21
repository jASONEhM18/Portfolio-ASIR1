'''calculadora básica'''
# input() toma lo que recoge del usuario como string
a1 = input("Introduce el primer número:")
a2 = input("Introduce el seguundo número:")
a = a1+a2
print(a)


# Solucionamos
a1 = input("Introduce el primero número:")
a1 = int(a1)

# otra manera
a2 = int(input("Introduce el segundo numero:"))

a = a1+a2
print(a)
######################################################
a1 = int(input("Introcude el primero número:"))
a2 = int(input("Introcude el segundo número:"))
suma = a1+a2
resta = a1-a2
multiplicacion = a1*a2
division = a1/a2


mensaje1 = f"Con los números introduciodos {a1} y {a2}, la suma es {suma}, la resta es {resta}, la multiplicacion es {multiplicacion}, y la división es {division}"
print(mensaje1)


# print(suma)
# print(resta)
# print(multiplicacion)
# print(division)

mensaje2 = f"""
Con los números introduciodos {a1} y {a2}, 
la suma es {suma}, 
la resta es {resta}, 
la multiplicacion es {multiplicacion}, 
y la división es {division}
"""

print(mensaje2)

'''Formato de variables tipo string'''
nombre = "Jason"
Apellido1 = "Huaracha"
Apellido2 = "Meléndez"

# Vamos a concatenar (unir) strings usando el operador +
# que si esta rodeado de string, los concatena

nombre_completo = nombre+Apellido1+Apellido2
print(nombre_completo)

nombre_completo = nombre+" "+Apellido1+" "+Apellido2
print(nombre_completo)

# se usa f "{}espacio en blanco {}" format()

nivel = "Fundamentos de"
tipo = "Programación"
lenguaje = "Python"
nombre_modulo = f"{nivel} {tipo} {lenguaje}"
print(nombre_modulo)

# Conseguir el siguiente texto GBD = 6 horas por semana
módulo = "Gestión de Bases de Datos"
dia1 = 1
dia2 = 3
dia3 = 2
datos_módulo = f"{módulo[0]}{módulo[11]}{módulo[20]} {"="} {dia1+dia2+dia3} {"horas por semana"}"


print(datos_módulo)

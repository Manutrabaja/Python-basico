# # Recorrer las claves de un diccionario
# estudiantes = {"Ana": 20, "Juan": 25, "Pedro": 30}
# for clave in estudiantes:
#     print(clave)

#     # Recorrer los valores de un diccionario
# estudiantes = {"Ana": 20, "Juan": 25, "Pedro": 30}
# for valor in estudiantes.values():
#     print(valor)

# # Recorrer pares clave-valor de un diccionario
# estudiantes = {"Ana": 20, "Juan": 25, "Pedro": 30}
# for clave, valor in estudiantes.items():
#     print(f"Clave: {clave}, Valor: {valor}")



# # Calcular la edad promedio de los estudiantes
# estudiantes = {"Ana": 20, "Juan": 25, "Pedro": 30}
# suma_edades = 0
# for edad in estudiantes.values():
#     suma_edades += edad

# promedio = suma_edades / len(estudiantes)
# print(f"Promedio de edad: {promedio:.2f}")

x = 0.0
for i in range(10):
    x += 0.1

if x == 1.0:
    print(f'x = {x}')
x = 0.0
for i in range(10):
    x += 0.1

if x == 1.0:
    print(f'x = {x}')
else:
    print(f'x != {x}')
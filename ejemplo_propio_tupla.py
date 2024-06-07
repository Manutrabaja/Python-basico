n = int(input('ingresa la un entero: '))

mi_tupla = (1, "Hola", 3.14, 54, "mi perro", "caro", 9.5)

def elemento_mi_tupla(n):
    resultado = mi_tupla[n]
    return resultado
print(elemento_mi_tupla(n))



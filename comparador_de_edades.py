nombre1 = input('ingresa un nombre: ')
nombre2 = input('ingresa un nombre: ')

num1 = print(nombre1), int(input('indicanos tu edad: '))
num2 = print(nombre2), int(input('dinos que edad tienes: '))

if num1 > num2:
    print(nombre1, 'es mayor que', nombre2)
elif num1 < num2:
    print(nombre2, 'es mayor que', nombre1)
else:
    print( nombre1, 'y', nombre2, 'tienen la misma edad')
# caculadore de raiz cuadrada exacta en numero enteros
    # Esta fuciona solo si el resultado es un numero entero..

objetivo =  int(input('Escoge un N° entero: '))
respuesta = 0

while respuesta**2 < objetivo:
    respuesta += 1
    print(respuesta)

if respuesta**2 == objetivo:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
else: 
    print(f'{objetivo} no tiene raiz cuadrada exacta')
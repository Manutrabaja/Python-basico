n = int(input('ingresa la un entero: '))

def numero_divicible_par(n):

        resultado = n % 2
        return resultado

if numero_divicible_par(n) == 0:
        print(f'Si {n} es una divicion entera {n/2}') 
else:
        print(f'{n} no es una divicion entera')
    
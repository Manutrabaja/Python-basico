# ---------------------------------- imprimiendo ramgo impares
""" muestra los numero impares de inicio a fin con el intervalo deseado
    
    Args:   inicio int >= 0  'inicio del rango' 
            fin int > inicio  'final del rango' 
            intervalo int >=2 'salto entre numeros'
        retrun imprime numeros impares
"""

def numero_divicible_par(i):

        resultado = i % 2
        return resultado

def imprime_impares(inicio, fin, intervalo):
    
    mi_segundo_rango = range(inicio, fin, intervalo)
    return mi_segundo_rango

inicio = int(input('ingresa la un N° de inicio: '))
fin = int(input('ingresa la un N° de final: '))
intervalo = int(input('ingresa la un N° de intervalo: '))

for i in imprime_impares(inicio, fin, intervalo):

    if numero_divicible_par(i) == True:
        print(i)
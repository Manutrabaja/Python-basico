# --------------------------------- imprime ramgos desde num1 a num2 con saltos de num3
""" genera rangos 
    num1 int >= 0 inicio
    num2 int > n final
    num3 int >=1 intervalo 
    return rango 
    """

def rango_definido(num1, num2, num3):
    
    mi_segundo_rango = range(num1, num2, num3)
    return mi_segundo_rango


num1 = int(input('ingresa la un N° de inicio: '))
num2 = int(input('ingresa la un N° de final: '))
num3 = int(input('ingresa la un N° de intervalo: '))

for i in rango_definido(num1, num2, num3):
    print(i)


        
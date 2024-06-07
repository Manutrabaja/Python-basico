# --------------------------------- imprime rangos desde 0 a n
""" genera rangos
    n int >= 1 
    retrun rango 0 a n
    """

def rango(n):
    
    mi_rango = range(n)
    return mi_rango


n = int(input('ingresa la un entero: '))
for numero in rango(n):
    print(numero)


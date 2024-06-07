def factorial(n):
    """ Calcula el factorial de n

    n int > 0
    retruns n!
    """
    print(n)
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
n = int(input('Introduce un N° entero: '))

print(factorial(n))
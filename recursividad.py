import sys
def factorial(n):
    """Calcula el factorial de n

    Args:
        n (int): > 0 

    Returns:
        factorial n!
    """
    if n ==1:
        print(n)
        return 1
    print(n)
    return n * factorial(n - 1)
n = int(input('Escribe un numero para sacar su factorial: '))
print(factorial(n))


def jugar(intento=1): 
    respuesta = input("¿De qué color es una naranja? ")
    if respuesta != "naranja": 
        if intento < 3: 
            print ("\nFallaste! Inténtalo de nuevo")
            intento += 1 
            jugar(intento) # Llamada recursiva 
        else: 
            print ("\nPerdiste!" )
    else:
        print ("\nGanaste!" )
jugar()



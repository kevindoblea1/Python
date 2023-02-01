def dividir_elementos(lista, divisor):
    """
    lista, es una lista para dividir
    divisor es el numero por el que se dividira
    """
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        return print("Realizo una division por 0, se devuelve la misma lista: \n" + str(lista))

lista = list(range(10))
divisor = 0
print(dividir_elementos(lista, divisor))
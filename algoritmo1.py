"""enameracion"""

num1 = int(input("Elige un entero: "))
respuesta = 0

while respuesta**2  < num1:
    respuesta+=1
if respuesta**2 == num1:
    print("La raiz cuadrada de " + str(num1) + " es " + str(respuesta))
else:
    print(str(num1) + " no tiene raiz cuadrada")
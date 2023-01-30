# range (inicio, fin, pasos)

mi_rango = range(1, 5)
type(mi_rango)
print(mi_rango)

mi_rango = range (0, 7, 2)
otro_rango = range(0, 8, 2)

mi_rango == otro_rango

for i in mi_rango:
    print(i)
    
for i in otro_rango:
    print(i)
    
print(id(mi_rango))
print(id(otro_rango))


"""Para comparar igualdad se debe usar el operador logico is"""
if mi_rango is otro_rango:
    print("Es lo mismo")
else:
    print("No son lo mismo")
    
for i  in range(0, 101, 2):
    print(i)
mi_lista = [1, 2, 3]
print("Lista de 3 elementos")
print(mi_lista)
print("___________________________________________________________")

"""Agregar elementos a la lista"""
print("Agregar elementos a la lista")
mi_lista.append(4)
print(mi_lista)
print("___________________________________________________________")

"""Eliminar elemento de la lista"""
print("Eliminar elementos a la lista")
mi_lista.pop()
print(mi_lista)
print("___________________________________________________________")

print("Iterar elementos de una lista usando for")
"""iterar elementos de una lista"""
for elements in mi_lista:
    print(elements)

"""la asignacion de valores a las listas solo hace que el apuntador use el mismo espacio en memoria"""
a =  [1, 2, 3]
b = a 

print(a)
print(b)

c = [a, b]
print(c)
print("___________________________________________________________")

"""Clonacion de listas"""

a = [1, 2, 3]
b = a
"""Usamos la funcion list"""
c = list(a)
print(c)
print("___________________________________________________________")
d = a [::]
print(d)
print(id(a))
print(id(c))
print(id(d))


nueva_lista = list(range(20))
double = [i * 2 for i in nueva_lista]
"""Sacamos los pares con el operador modulo"""
pares = [i for i in nueva_lista if i % 2 == 0]
print(double)
print(pares)
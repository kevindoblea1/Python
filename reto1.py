name1 = (input("Primer persona ingrese su nombre: "))
edad1 = int(input("Ahora ingrese su edad: "))
name2 = (input("Segunda persona ingrese su nombre: "))
edad2 = int(input("Ahora ingrese su edad: "))

if edad1 > edad2:
    print(str(name1) + ' eres mayor que ' + str(name2))
elif edad2 > edad1:
    print(str(name2) + ' eres mayor que ' + str(name1))
else:
    print("Ambos tienen " + str(edad1) + ' años') 
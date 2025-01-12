a = 2
b = 2

if a < b:
    print("A es menor que B")
elif a == b:
    print("A es igual a B")
else:
    print("A es mayor que B")
    
    
a = False

if a:
    print("A es verdadero")
else:
    print("A es falso")

a = True

if type(a) is bool:
    print("A es un booleano")
else:
    print("A es otro tipo de dato")
    

a = 10
b = 5
c = 1

if a > b or b > c:
    print("Las dos condiciones son verdaderas")
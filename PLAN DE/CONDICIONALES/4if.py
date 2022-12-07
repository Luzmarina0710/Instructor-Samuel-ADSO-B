a = int(input("escriba un nro: "))
b = int(input("escriba un nro: "))


if a > b:
    mayor = a
elif b > a:
    mayor = b
else:
    mayor = "iguales"
    
print ("el numero mayor es:",mayor)
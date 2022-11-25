from fractions import Fraction

print("fracciones")

n1 = Fraction(input("introduce un numero fraccionario, ejemplo 5/8: "))
print(n1)

n2 = Fraction(input("introduce otro numero fraccionario, ejemplo 2/4: "))
print(n2)

print("El resultado de la suma es: " + str(n1+n2))
print("El resultado de la resta es:" + str(n1-n2))
print("El resultado de la multiplicacion es: " +str(n1*n2))
print("El resultado de la division es: " + str(n1/n2))
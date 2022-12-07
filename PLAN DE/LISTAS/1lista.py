import random

list =[ random.randint(1,10) for i in range(10)]
print(list)

suma = 0
for i in list:
    suma += i
print(suma)
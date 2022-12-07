frase = input("escriba un nombre: ")

def longitud(a):
    cont = 0
    for i in a:
        cont += 1
    return cont

print(longitud(frase))
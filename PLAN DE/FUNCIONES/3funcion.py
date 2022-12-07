radio = float(input('cual es el radio del circulo? '))
altura = float(input('cual es la altura del cilindro? '))

def area_circulo(radio):
    pi = 3.1415
    return pi*radio**2

def volumen(radio, altura):
    return area_circulo(radio) * altura

print(volumen(radio,altura))
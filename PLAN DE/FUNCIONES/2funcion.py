"""Función de aplica el IVA a una factura.
    Parametros
    precio: Es la cantidad sin IVA
    vat: Es el porcentaje de IVA
    Devuelve el total de la factura una vez aplicado el IVA. 
    """
n = int(input('escriba el precio '))

def iva(precio, iva):
    
    return precio + precio * iva/100

print(iva(n,iva=21))
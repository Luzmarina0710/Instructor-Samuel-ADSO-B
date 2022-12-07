nombre = input("Escriba su nombre: ")
genero = input("¿Escriba su genero (M o H)? ")
if genero == "M":
    if nombre.lower() < "m":
        group = "A"
    else:
        group = "B"
else:
    if nombre.lower() > "h":
        group = "A"
    else:
        group = "B"
print("Tu grupo es " + group)
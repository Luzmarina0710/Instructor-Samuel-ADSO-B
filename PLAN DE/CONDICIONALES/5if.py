edad = int(input("¿Cuál es tu edad? "))
salario = int(input("¿Cuales son tus ingresos mensuales? "))

if edad > 18 and salario >= 1000:
    print("Tienes que cotizar")
else:
    print("No tienes que cotizar")
from math import pi

radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))

if altura > radio:
    volumen = pi * radio**2 * altura
    print("El volumen del cilindro es:", volumen)
else:
    area = 2 * pi * radio * (radio + altura)
    print("El área del cilindro es:", area)

from math import pi

radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))

if altura > radio:
    volumen = pi * radio**2 * altura
    print("El volumen del cilindro es:", volumen)
else:
    print("Error: la altura no es mayor al radio")

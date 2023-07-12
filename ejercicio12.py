numero = int(input("Ingrese un número entre 0 y 10: "))

if numero >= 0 and numero <= 10:
    if numero % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")
else:
    print("El número no está comprendido entre 0 y 10.")

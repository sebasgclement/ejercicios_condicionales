temperatura = float(input("Ingrese el valor de temperatura: "))
codigo = int(input("Ingrese el código (1 o 2): "))

if codigo == 1:
    temperatura_c = (5 / 9) * (temperatura - 32)
    print("La temperatura convertida a grados Celsius es:", temperatura_c)
elif codigo == 2:
    temperatura_f = (9 / 5) * temperatura + 32
    print("La temperatura convertida a grados Fahrenheit es:", temperatura_f)
else:
    print("Error: código no válido.")

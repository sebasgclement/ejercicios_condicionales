lado1 = float(input("Ingrese la longitud del lado 1: "))
lado2 = float(input("Ingrese la longitud del lado 2: "))
lado3 = float(input("Ingrese la longitud del lado 3: "))

# Verificar el tipo de triángulo
if lado1 == lado2 == lado3:
    tipo_triangulo = "Equilátero"
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    tipo_triangulo = "Isósceles"
else:
    tipo_triangulo = "Escaleno"

# Mostrar el tipo de triángulo
print("El triángulo es de tipo:", tipo_triangulo)

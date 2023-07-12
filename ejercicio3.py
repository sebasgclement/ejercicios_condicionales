from math import sqrt

ancho = float(input("Ingrese el ancho del bloque: "))
alto = float(input("Ingrese la altura del bloque: "))
largo = float(input("Ingrese el largo del bloque: "))

diagonal_1 = sqrt(ancho**2 + alto**2)
diagonal_2 = sqrt(ancho**2 + largo**2)
diagonal_3 = sqrt(alto**2 + largo**2)

mayor_diagonal = max(diagonal_1, diagonal_2, diagonal_3)

print("La mayor diagonal del bloque es:", mayor_diagonal)

may1, may2 = -1
may1_2, may2_2 = -1
#notas del primer estudiante
ne1 = float(input("Ingrese la primer nota del primer estudiante: "))
ne2 = float(input("Ingrese la primer nota del primer estudiante: "))
ne3 = float(input("Ingrese la primer nota del primer estudiante: "))

#Generamos las comparaciones y el promedio para el primer estudiante
if ne1 > ne2 and ne1> ne3:
    may1=ne1
elif ne2 > ne1 and ne2> ne3:
    may1=ne2
else:
    may1= ne3

if ne1 == may1:
    if ne2 > ne3:
        may2=ne2
    else:
        may2 = ne3
elif ne2 == may1:
    if ne1 > ne3:
        may2=ne1
    else:
        may2 = ne3
elif ne3 == may1:
    if ne1 > ne2:
        may2=ne1
    else:
        may2 = ne2

promedio_e1 = may1 + may2

#notas del segundo estudiante
ne1_2 = float(input("Ingrese la primer nota del primer estudiante: "))
ne2_2 = float(input("Ingrese la primer nota del primer estudiante: "))
ne3_2 = float(input("Ingrese la primer nota del primer estudiante: "))

#Generamos las comparaciones y el promedio para el segundo estudiante
if ne1_2 > ne2_2 and ne1_2> ne3_2:
    may1_2=ne1_2
elif ne2_2 > ne1_2 and ne2_2> ne3_2:
    may1_2=ne2_2
else:
    may1_2= ne3_2

if ne1_2 == may1_2:
    if ne2_2 > ne3_2:
        may2_2=ne2_2
    else:
        may2_2 = ne3_2
elif ne2_2 == may1_2:
    if ne1_2 > ne3_2:
        may2_2=ne1_2
    else:
        may2_2 = ne3_2
elif ne3_2 == may1_2:
    if ne1_2 > ne2_2:
        may2_2=ne1_2
    else:
        may2_2 = ne2_2

promedio_e2 = may1_2 + may2_2

#Comparamos los promedios de ambos estudiantes

if promedio_e1 > promedio_e2:
    print("El estudiante 1 tiene el mayor promedio ")
elif promedio_e2 > promedio_e1:
    print("El estudiante 2 tiene el mayor promedio ")
else:
    print("Ambos estudiantes tienen el mismo promedio ")
numero = float(input("Ingrese un número: "))

es_entero = numero.is_integer()
es_multiplo_de_7 = numero % 7 == 0

if es_entero and es_multiplo_de_7:
    mensaje = "El número ingresado es un número entero y es múltiplo de 7."
elif es_entero:
    mensaje = "El número ingresado es un número entero pero no es múltiplo de 7."
elif es_multiplo_de_7:
    mensaje = "El número ingresado no es un número entero pero es múltiplo de 7."
else:
    mensaje = "El número ingresado no es un número entero y no es múltiplo de 7."

print(mensaje)

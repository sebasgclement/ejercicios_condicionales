kw_consumidos = float(input("Ingrese la cantidad de Kw consumidos: "))
precio_kw = float(input("Ingrese el precio por Kw: "))

if kw_consumidos > 700:
    exceso_kw = kw_consumidos - 700
    incremento_precio = exceso_kw * (precio_kw * 0.05)
    total_pagar = (700 * precio_kw) + incremento_precio
else:
    total_pagar = kw_consumidos * precio_kw

print("El valor total a pagar es:", total_pagar)

precios = [50, 75, 46, 22, 80, 65, 8]
min = max = precios[0]
for precio in precios:
    if precio < min:
        min = precio
    elif precio > max:
        max = precio
print("El precio máximo es " + str(max))
print("El precio mínimo es " + str(min))


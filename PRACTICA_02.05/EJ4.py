ganadores = []
for a in range(6):
    ganadores.append(int(input("Introduce los números de los ganadores: ")))
ganadores.sort()
print("Los números de los ganadores son: " + str(ganadores))
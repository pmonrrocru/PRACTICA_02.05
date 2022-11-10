asignaturas = ["Sirc", "Rete", "Dapi", "Gpit", "Sipa", "Eiem", "Sihd"]
suspendidas = []
for asignatura in asignaturas:
    nota_asignatura = float(input("Introduce la nota que has sacado en " + asignatura + ": "))
    if nota_asignatura < 5:
        suspendidas.append(asignatura)
        for asignatura in suspendidas:
            print("Tienes que repetir: " + asignatura)



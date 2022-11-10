lista_asignaturas = ["Sirc", "Rete", "Dapi", "Gpit", "Sipa", "Eiem", "Sihd"]
for asignatura in lista_asignaturas:
  notas_asignaturas = input("Introduce tu nota de " + asignatura + ": ")
  for nota in notas_asignaturas:
   print("En " + asignatura + " has sacado " + nota)
palabra = input("Introduce una palabra para contar sus vocales: ")
vocales = ["a", "e", "i", "o", "u"]
for vocal in vocales:
    veces = 0
    for letra in palabra:
        if letra == vocal:
            veces += 1
    print(vocal + " aparece " + str(veces) + " veces en " + palabra)

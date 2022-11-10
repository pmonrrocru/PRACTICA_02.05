abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
for a in range(len(abecedario), 1, -1):
        if a % 3 == 0:
            abecedario.pop(a-1)
print(abecedario)
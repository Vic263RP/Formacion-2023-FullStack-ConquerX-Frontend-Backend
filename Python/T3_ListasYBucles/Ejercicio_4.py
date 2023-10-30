phrase = input("Introduzca una frase: ")
letter = input("Introduzca una letra: ")
n_veces = 0

for caracter in range(0,len(phrase)):
    if phrase[caracter] == letter:
        n_veces += 1

print(f"La letra {letter} se repite {n_veces} veces")
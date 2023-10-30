
palabras_aleatorias = ["casa", "rasa", "corro", "libro", "sesgo"]
letras_prohibidas = ["c", "e", "s"]
lista_filtrada = []


for palabra in palabras_aleatorias:
    for letra in letras_prohibidas:
        if letra not in palabra and palabra not in lista_filtrada:
            lista_filtrada.append(palabra)
        if letra in palabra and palabra in lista_filtrada:
            lista_filtrada.remove(palabra)
            break

print(lista_filtrada)
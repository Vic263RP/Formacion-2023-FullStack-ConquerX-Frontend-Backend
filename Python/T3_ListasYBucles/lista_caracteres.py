frutas = ["manzana", "plátano", "cereza", "pera", "higo", "frambuesa", "fresa"]

print(len(frutas))
print(frutas[2])
frutas[1] = "mora"

frutas.append("mango")

frutas.insert(0, "uva")

for fruta in frutas:
    print(fruta, end = " ")
print("\n")

ultima_fruta = frutas.pop()

for fruta in frutas:
    print(len(fruta), end = " ")
print("\n")

for fruta in frutas:
    if len(fruta) > 5:
        print(fruta, end = " ")
print("\n")

frutas.remove("cereza")

frutas.clear()

print(frutas)
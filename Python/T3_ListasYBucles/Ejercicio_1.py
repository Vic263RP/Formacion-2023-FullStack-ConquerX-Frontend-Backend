n_centro = int(input("Elige el número de estrellas que quieres: "))

for i in range(1,n_centro+1):
    print("*"*i)

for i in range(n_centro-1,0,-1):
    print("*"*i)

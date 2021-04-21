lista = []
quad = []
for n in range(10):
    lista.append(int(input("Número: ")))
    quad.append(lista[n] * lista[n])
print("Os números digitados foram {}\nE seus respectivos quadrados são {}" .format(lista, quad))

listcod = []
listnom = []
listnum = []

for c in range(100):
    listcod.append(input("Código: "))
    listnom.append(str(input("Nome: ")))
    listnum.append(int(input("Número: ")))

while True:
    p = input("Faça a pesquisa: ")
    if p in listcod:
        c=listcod.index(p)
        print(listnom[c], listnum[c])
    else:
        print("Este código não foi encontrado")
    s = input("Quer continuar? ")
    if s in "Nn":
        break
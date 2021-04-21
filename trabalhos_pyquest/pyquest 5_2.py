listmat = []

for m in range(100):
    listmat.append(input("Matricula: "))
    listmat.append(float(input("Salario: ")))
    listmat.append((listmat[1] * 11)/100)
    listmat.append((listmat[1] - listmat[2]))

print(f' os dados foram {listmat}')

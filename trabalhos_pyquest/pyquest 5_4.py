listnom = []
listnot = []
media = 0
alunos = 10

for n in range(alunos):
    listnom.append(str(input("Nome: ")))
    listnot.append(float(input("Nota: ")))
    media = media + listnot[n]

media = media / alunos
print(" A média da turma é {}." .format(media))

for n in range(alunos):
    if listnot[n] > media:
        print(listnom[n], listnot[n])
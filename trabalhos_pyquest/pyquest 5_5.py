listnum = []

for n in range(10):
    listnum.append(int(input("Numero: ")))
    
listnum.sort()
print(f' Os números em ordem crescente ficam {listnum}')

listnum.reverse()
print(f' Os números em ordem decrescente ficam {listnum}')
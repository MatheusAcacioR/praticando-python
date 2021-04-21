listanum = []
listanom = []
for c in range(50):
    num = float(input(f'Altura: '))
    nom = str(input(f'nome: '))
    if num > 1.70:
        listanum.append(num)
        listanom.append(nom)
print(f'As pessoas maiores que 1,70 são {listanom} e tem alturas respectivas {listanum}. ')
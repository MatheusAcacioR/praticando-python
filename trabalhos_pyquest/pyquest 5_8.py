listanum = []
maior = 0
menor = 0

for n in range(9):
    listanum.append(int(input("Número: ")))
    if n == 0:
        maior = menor = listanum[n]
    else:
        if listanum[n] > maior:
            listanum[n] = maior
        elif listanum[n] < menor:
            listanum[n] = menor
print("Você digitou os valores {}" .format(listanum))
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i} ', end='')
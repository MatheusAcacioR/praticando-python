matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}] '))

print('-+' * 30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^3}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c] # se o valor dessa posição da matriz for par, ele sera adicionado na soma dos valores pares da matriz
    print()

print('-+' * 30)
print(f'A soma dos valores pares é {spar}')

for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da coluna 3 é {scol}')

for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]

print(f'O maior valor da coluna dois é {mai}')
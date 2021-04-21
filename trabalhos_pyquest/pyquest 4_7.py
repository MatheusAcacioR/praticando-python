num = int(input("Numero: "))
quant = maior = menor = 0

while num != 0:
    num = int(input("Numero: "))
    quant = quant + 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print("O maior número é {}." .format(maior))



quant = par = ímpar = 0
num = int(input("Número: "))

while num != 0:
    num = int(input("Número: "))
    quant = quant + 1
    if num % 2 == 0:
        par = par + 1
    if num % 2 == 1:
        ímpar = ímpar + 1

print("A quantidade de valores digitados foi {}.\nOs valores pares foram {}.\nOs valores ímpares foram {}." .format(quant, par, ímpar))

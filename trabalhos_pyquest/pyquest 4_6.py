ida = int(input('Idade: '))
i1 = 0
i2 = 0
i3 = 0

while (ida != 0):
    ida = int(input("Idade: "))
    i1 = i1 + 1
    if ida < 18:
        i2 = i2 + 1
    elif ida >= 18:
        i3 = i3 + 1

p2 = (i2 * 100)/i1
p3 = (i3 * 100)/i1

print("O total de pessoas cadastradas é {}.\nA porcentagem de pessoas menores que 18 é {}%.\nA porcentagem de pessoas maiores ou igual a 18 é {}%." .format(i1, p2, p3))
alt = float(input("Altura: "))
c1 = 0
alt1 = 0
alt2 = 0
alt3 = 0
while (alt != 0):
    alt = float(input("Altura: "))
    c1 += 1
    if alt < 1.60:
        alt1 += 1
    elif alt >= 1.60 and alt <= 1.80:
        alt2 += 1
    elif alt > 1.80:
        alt3 += 1
print("O total de cadastrados é {}.\n O total de pessoas menores que 1.60 é {}.\n O total de pessoas entre 1,60 e 1.80 é {}.\nO total de pessos acima de 1.80 é {}." .format(c1, alt1, alt2, alt3))
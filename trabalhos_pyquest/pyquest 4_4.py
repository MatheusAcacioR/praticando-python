sex = ""
c1 = 0
m1 = 0
g1 = 0
while (sex != "S"):
    sex = str(input("Sexo; "))
    c1 += 1
    if sex == "m":
        m1 += 1
    elif sex == "f":
        g1 += 1
    scape = str(input("Deseja sair?[sim/não]"))
    if scape == "sim":
        break
print("O número de pessoas cadastradas foram {}.\nO número de pessoas cadastradas do sexo masculino foram {}\nO número de pessoas cadastradas do sexo feminino foram {}." .format(c1, m1, g1))
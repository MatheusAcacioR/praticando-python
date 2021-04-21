f = "P"
somai = 0
w = 0
y = 1
while (f != "s"):
    i = int(input("idade: "))
    somai += i
    f = input("Digite s para sair")
    w += y
med = somai/w
print("A soma das idades é {}.\nA média das idades é {}." .format(somai, med))


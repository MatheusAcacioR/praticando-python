soma = 0
for p in range(0, 11):
    preco = float(input("Preço: "))
    soma = soma + preco
print("A soma do preço dos produtos foi R$ {}." .format(soma))
print(f"A soma do preço dos produtos foi R$ {soma}.")
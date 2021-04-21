# input pro usuario digitar a cadeia de nucleotideos e adicionando ele na variavel base
base = str(input("Digite as bases de nucleotideos: "))
base = base.upper() # converter a string em "Caixa alta" caso o usuario digite alguma base em letra minuscula
base = base.split() # faz um split na strind para separar cada cadeia e adiciona-los em um array
scape = False

conterBase = [] # array vazio para armazenar as bases da contra-cadeia

# para cada base de nucletideo da cadeira principal, ele ira adicionar no array da contra-cadeia as bases correspondentes
for x in base:
    if x == 'A':
        conterBase.append('T')
    elif x == 'T':
        conterBase.append('A')
    elif x == 'C':
        conterBase.append('G')
    elif x == 'G':
        conterBase.append('C')

print(base)
print(conterBase)
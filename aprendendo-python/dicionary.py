dicionario = {                 # CRIANDO O DICIONARIO E COLOCANDO ITENS NELE
    "carro": "É um veiculo",
     2: True, 
     "alimentos": {
        "Banana": "Fruta", 
        "Bolacha": "Biscoito", 
        "Pen-Drive": False
    }
}

a = dicionario['carro']  # ACESSANDO O VALOR DO ITEM 1 DO DICIONARIO
b = dicionario[2]  # ACESSANDO O VALOR DO ITEM 2 DO DICIONARIO
c = dicionario['alimentos']  # ACESSANDO OS VALORES DO ITEM 3 DO DICIONARIO - DICIONARIO DE DICIONARIO

c1 = dicionario['alimentos']['Banana'] # ACESSANDO O VALOR DO ITEM 1 DO ITEM 3 QUE É UM DICIONARIO QUE ESTA DENTRO DO PRIMEIRO DICIONARIO
c2 = dicionario['alimentos']['Bolacha'] # ACESSANDO O VALOR DO ITEM 2 DO ITEM 3 QUE É UM DICIONARIO QUE ESTA DENTRO DO PRIMEIRO DICIONARIO
c3 = dicionario['alimentos']['Pen-Drive'] # ACESSANDO O VALOR DO ITEM 3 DO ITEM 3 QUE É UM DICIONARIO QUE ESTA DENTRO DO PRIMEIRO DICIONARIO


print(a)
print(b)
print(c)

print(c1)
print(c2)
print(c3)
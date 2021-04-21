listnum = []
neg = nul = pos = 0

for n in range(10):
    listnum.append(int(input("Número: ")))
    if listnum[n] < 0:
        neg += 1
    elif listnum[n] == 0:
        nul += 1
    else:
        pos += 1

print("A quantidade de negativos da lista são {}\nA quantidade de nulos na lista são {}\nA quantidade de positivos na lista são {}" .format(neg, nul, pos))
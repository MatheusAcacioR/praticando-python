a = []
b = []
c = []
for i in range (1,11):
    a.append(int (input (f'{i} - Digite um número para tabela A:')))
    b.append(int (input (f'{i} - Digite um número para tabela B:')))
    c.append(a[i] + b[i])

print ('Tabela A - {}'.format(a))
print ('Tabela B - {}'.format(b))
print ('Tabela C - {}'.format(c))
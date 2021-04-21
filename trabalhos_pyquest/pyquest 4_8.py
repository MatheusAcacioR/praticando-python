maior = menor = p = soma = 0

for p in range(0, 11):
    nom = input("nome: ")
    alt = float(input("idade: "))
    soma = soma + alt
    if p == 1:
        m_alta = alt
        n_alta = nom
    else:
        if alt > maior:
            maior = m_alta = alt
            n_alta = nom

print("{1} é a pessoa mais alta e tem {0} m." .format(m_alta, n_alta))

# Capturando a resposta do input e processando-a
def resposta():
    resp = input('>: ')
    resp = resp.lower()
    resp = resp.replace('é', 'eh')
    return resp

def pegaNome(nome):
    if 'o meu nome eh ' in nome:
        nome = nome[14: ]

    nome = nome.title()
    return nome

def respondeNome(nome):
    conhecidos = ['Raimundo', 'Will', 'João']

    if nome in conhecidos:
        frase = 'Eaew'
    else:
        frase = 'Muito prazer '

    return frase+nome
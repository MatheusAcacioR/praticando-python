"""
return retorna o valor que se encontra dentro da variavel
sem o return a função ira retornar o tipo da variavel e nao o seu valor

"""

def funcao(var):
    return var

variavel = funcao('Aqui tem um valor')

"""if variavel:
    print(variavel)
else:
    print('Nenhum valor')"""


"""
Se nao passar os parenteses da funcao ira retornar a funcao, para retornar
o que a função faz de fato deve-se passar os parentes

"""
print(funcao, type(funcao))
print(funcao(1), type(funcao(1)))

def f(var):
    print(var)

def dumb():
    return f

var = dumb()
var('Pode imprimir algo na tela')
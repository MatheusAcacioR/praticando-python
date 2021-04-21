print('Ola bem vindo ao atendimento ao cliente, qual o seu nome?')

nome = input('Meu nome é ')

print(f'Muito prazer {nome}')
print("""Escolha a opcao de atendimento
[1] - Financeiro
[2] - Avaliação
[3] - Sujestões de melhorias de atendimento""")

opcao = int(input())

if opcao == 1:
    print("""Muito bem, vc escolheu falar com o financeiro
Aguarde um momento que iremos te encaminhar....""")
elif opcao == 2:
    print("""Muito bem, vc escolheu falar com a Avaliação
Aguarde um momento que iremos te encaminhar....""")
elif opcao == 3:
    print("O que gostaria de nos sugerir? Estamos abertos a qualquer tipo de sujestão")
    str(input())
    print("Muito obrigado!! Gostamos muito de ter ouvido sua opnião sobre nós")
else:
    print("""Desculpe, essa opção não é reconhecida por nós.
Vamos te encaminhar para um atendente físico....""")
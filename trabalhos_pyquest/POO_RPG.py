from pyRPG import *

print("""Personagens:
""")

p1 = Personagem("Personagem 1", "A cada metro aumenta 1 de ataque", "Velocidade sonica","Corrida que causa dano aos inimigos dentro do alcance", "Assassino", 1100, 300, 400, 700)
p2 = Personagem("Personagem 2", "Dano causado aos inimigos recupera vida de aliados próximos", "Aurea curadora", "Cria um campo ao redor dela que recupara 10 HP por segundo durante 10 segundos", "Paladino", 1500, 200, 500, 450)
p3 = Personagem("Personagem 3", "A cada aliado dentro da redoma o ataque aumwenta em 10", "Fortificando", "Redoma que aumenta os atributos dos aliados proximos", "Mago", 1000, 500, 300, 400)

print(f"""Nome: {p1.nome}          
Passiva: {p1.passiva}
Habilidade: {p1.habilidade_especial}
Descrição: {p1.descricao}
Classe: {p1.classe}
Vida: {p1.vida}
Ataque:{p1.ataque}
Defesa:{p1.defesa}
Mobilidade:{p1.mobilidade}
""")
x = input("")
print(f"""Nome: {p2.nome}
Passiva: {p2.passiva}
Habilidade: {p2.habilidade_especial}
Descrição: {p2.descricao}
Classe: {p2.classe}
Vida: {p2.vida}
Ataque:{p2.ataque}
Defesa:{p2.defesa}
Mobilidade:{p2.mobilidade}
""")
y = input("")
print(f"""Nome: {p3.nome}
Passiva: {p3.passiva}
Habilidade: {p3.habilidade_especial}
Descrição: {p3.descricao}
Classe: {p3.classe}
Vida: {p3.vida}
Ataque:{p3.ataque}
Defesa:{p3.defesa}
Mobilidade:{p3.mobilidade}
""")
z = input("")
while True:
    escolha = input("Escollha seu personagem: ")
    if escolha == "Personagem 1":
        seu_personagem = p1
        print(f"""Você escolheu {p1.nome}
""")
        break
    elif escolha == "Personagem 2":
        seu_personagem = p2
        print(f"""Você escolheu {p2.nome}
""")
        break
    elif escolha == "Personagem 3":
        seu_personagem = p3
        print(f"""Você escolheu {p3.nome}
""")
        break
    else:
        print(f"Este personagem não exite....escolha novamente!")

w = input(" ")

print(f"""Capacete 1             Capacete 2             Capacete 3                   
Nome: {seu_personagem.nome}             Nome: {seu_personagem.nome}             Nome: {seu_personagem.nome}
Vida: {seu_personagem.vida}             Vida: {seu_personagem.vida}             Vida: {seu_personagem.vida} + 200
Ataque:{seu_personagem.ataque} + 100       Ataque:{seu_personagem.ataque}             Ataque:{seu_personagem.ataque}
Defesa:{seu_personagem.defesa} + 210       Defesa:{seu_personagem.defesa} - 100       Defesa:{seu_personagem.defesa} - 100
Mobilidade:{seu_personagem.mobilidade}         Mobilidade:{seu_personagem.mobilidade} - 320   Mobilidade:{seu_personagem.mobilidade}""")

escolha2 = input("""Agora é hora de se equipar, começando pelo capacete.
Qual você escolhe?
""")

if escolha2 == "Capacete 1":
    seu_personagem.capacete1()
elif escolha2 == "Capacete 2":
    seu_personagem.capacete2()
elif escolha2 == "Capacete 3":
    seu_personagem.capacete3()

print(f"""Peitoral 1             Peitoral 2             Peitoral 3                   
Nome: {seu_personagem.nome}             Nome: {seu_personagem.nome}             Nome: {seu_personagem.nome}
Vida: {seu_personagem.vida}             Vida: {seu_personagem.vida}             Vida: {seu_personagem.vida} + 330
Ataque:{seu_personagem.ataque}             Ataque:{seu_personagem.ataque} + 580       Ataque:{seu_personagem.ataque}
Defesa:{seu_personagem.defesa} + 400       Defesa:{seu_personagem.defesa} - 100       Defesa:{seu_personagem.defesa} + 210
Mobilidade:{seu_personagem.mobilidade} - 250   Mobilidade:{seu_personagem.mobilidade} - 100   Mobilidade:{seu_personagem.mobilidade}""")

escolha3 = input("""Agora é hora de escolher seu peitoral. Qual você escolhe?
""")

if escolha3 == "Peitoral 1":
    seu_personagem.peitoral1()
elif escolha3 == "Peitoral 2":
    seu_personagem.peitoral2()
elif escolha3 == "Peitoral 3":
    seu_personagem.peitoral3()

print(f"""Manopla 1             Manopla 2             Manopla 3                   
Nome: {seu_personagem.nome}             Nome: {seu_personagem.nome}             Nome: {seu_personagem.nome}
Vida: {seu_personagem.vida} - 300       Vida: {seu_personagem.vida}             Vida: {seu_personagem.vida} - 430
Ataque:{seu_personagem.ataque}             Ataque:{seu_personagem.ataque} - 100       Ataque:{seu_personagem.ataque}
Defesa:{seu_personagem.defesa}             Defesa:{seu_personagem.defesa}             Defesa:{seu_personagem.defesa} + 200
Mobilidade:{seu_personagem.mobilidade} + 400   Mobilidade:{seu_personagem.mobilidade} + 200   Mobilidade:{seu_personagem.mobilidade}""")

escolha4 = input("""Agora é hora de escolher suas manoplas. Qual você escolhe?
""")

if escolha4 == "Manopla 1":
    seu_personagem.manopla1()
elif escolha4 == "Manopla 2":
    seu_personagem.manopla2()
elif escolha4 == "Manopla 3":
    seu_personagem.manopla3()

print(f"""Greva 1             Greva 2             Greva 3                   
Nome: {seu_personagem.nome}             Nome: {seu_personagem.nome}             Nome: {seu_personagem.nome}
Vida: {seu_personagem.vida}             Vida: {seu_personagem.vida} + 200       Vida: {seu_personagem.vida} 
Ataque:{seu_personagem.ataque} + 300       Ataque:{seu_personagem.ataque}             Ataque:{seu_personagem.ataque}
Defesa:{seu_personagem.defesa}             Defesa:{seu_personagem.defesa}             Defesa:{seu_personagem.defesa} - 100
Mobilidade:{seu_personagem.mobilidade} - 160   Mobilidade:{seu_personagem.mobilidade} + 440   Mobilidade:{seu_personagem.mobilidade} + 300""")

escolha5 = input("""Agora é hora de escolher suas Grevas. Qual você escolhe?
""")

if escolha5 == "Greva 1":
    seu_personagem.greva1()
elif escolha5 == "Greva 2":
    seu_personagem.greva2()
elif escolha5 == "Greva 3":
    seu_personagem.greva3()

print("""Muito bem! Agora você esta devidamente equipado.
""")

print(f"""Nome: {seu_personagem.nome}
Vida: {seu_personagem.vida}
Ataque: {seu_personagem.ataque}
Defesa: {seu_personagem.defesa}
Mobilidade: {seu_personagem.mobilidade}""")
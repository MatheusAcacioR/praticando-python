class Personagem:

    def __init__(self, nome, passiva, habilidade_especial, descricao, classe, vida, ataque, defesa, mobilidade):
        self.nome = nome
        self.passiva = passiva
        self.habilidade_especial = habilidade_especial
        self.descricao = descricao
        self.classe = classe
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.mobilidade = mobilidade



    def capacete1(self):
        self.ataque += 100
        self.defesa += 210

    def capacete2(self):
        self.mobilidade -= 320
        self.defesa -= 100

    def capacete3(self):
        self.vida += 200
        self.defesa -= 100



    def peitoral1(self):
        self.mobilidade -= 250
        self.defesa += 400

    def peitoral2(self):
        self.ataque += 580
        self.mobilidade -= 100

    def peitoral3(self):
        self.vida += 330
        self.defesa += 210



    def manopla1(self):
        self.mobilidade += 400
        self.vida -= 300

    def manopla2(self):
        self.ataque -= 100
        self.mobilidade += 200

    def manopla3(self):
        self.defesa += 200
        self.vida -= 430



    def greva1(self):
        self.ataque += 300
        self.mobilidade -= 160

    def greva2(self):
        self.mobilidade += 440
        self.vida += 200

    def greva3(self):
        self.mobilidade += 300
        self.defesa -= 100
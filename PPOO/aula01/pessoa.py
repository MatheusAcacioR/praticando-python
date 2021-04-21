from datetime import datetime

# Molde para criaçã de uma pessoa com seus devidos atributos(parametros) e o atributo principal self
class Pessoa: 
    currentYear = int(datetime.strftime(datetime.now(), '%Y'))

    # Ultiliza-se funções para definir metodos que sao determinadas caracteristicas de uam pessoa
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        # Se comer for verdade entao pessoa nao pode falar comendo
        if self.comendo:
            print(f'{self.nome} nao pode falar comendo')
            return

        # Se falar ja for verdade entao pessoa nao pode falar outra coisa
        if self.falando:
            print(f'{self.nome} já esta falando.')
            return

        # Do contrario falar é falso entao pessoa pode falar
        self.falando = True
        print(f'{self.nome} diz "{assunto}".')

    def pararDeFalar(self):

        # Se falar nao for verdadeiro pessoa nao estara falando
        if not self.falando:
            print(f'{self.nome} não esta falando.')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False

    def comer(self, alimento):
        # Caso ja esteja comendo, mostra o print que a pessoa ja esta comendo
        if self.comendo:
            print(f'{self.nome} já esta comendo.')
            return

        # Se falar for verdadeiro entao pessoa nao pode comer enquanto fala
        if self.falando:
            print(f'{self.nome} não pode comer falando')
            return
        # definindo o parametro como True apresenta que a pessoa esta comendo e mostra o print que a pessoa esta comendo e o que ela esta comendo
        self.comendo = True
        print(f'{self.nome} esta comendo {alimento}.')

    def pararDeComer(self):
        # Se ele nao estiver comendo nao tem como fazer ele parar de comer
        if not self.comendo:
            print(f'{self.nome} não esta comendo.')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def getBirthDate(self):
        return self.currentYear - self.idade
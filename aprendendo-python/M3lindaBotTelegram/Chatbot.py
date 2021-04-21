import json
import sys
import os
import subprocess as s

class Chatbot():
    def __init__(self, nome):
        try: # TENTOU EXECUTAR O COMANDO ABAIXO
            memoria = open(nome + '.json', 'r') # ABRIU O ARQUIVO PARA LEITURA
        except FileNotFoundError: # CASO NÃO FOSSE POSSIVEL EXECUTAR O COMANDO ABAIXO
            memoria = open(nome + '.json', 'w') # CRIOU UM ARQUIVO PARA ESCRITA
            memoria.write('[["Will", "Alfredo"], {"oi": "Ola, qual o seu nome?", "tchau": "tchau"}]') # ESCREVEU NO ARQUIVO 
            # DICIONARIO COM FRASES DE PERGUNTA QUE O USUARIO IRA FAZER E A RESPOSTA QUE O BOT DARA
            memoria.close() # FECHOU O ARQUIVO
            memoria = open(nome + '.json', 'r') # ABRIU O ARQUIVO PARA LEITURA
        self.nome = nome
        self.conhecidos, self.frases = json.load(memoria) # MULTIPLAS ATRIBUIÇOERS DE VARIAVIES A MEMORIA - A PRIMERIA É A MEMORIA DE NOMES DE PESSOAS CONHECIDAS E SEGUNDA DE FRASES E SUA RESPOSTAS 
        # ARMAZENOU OS NOMES DA ARQUIVO DE MOMORIA DO CHATBOT NA LISTA DE CONHECIDOS
        memoria.close() # FECHOU O ARQUIVO 
        self.historico = [None, ]

    def escuta(self, frase = None): # ENTRADA DE FALA DO USUARIO E TRATAMENTO DA FRASE
        if frase == None: # COM A INTEGRAÇÃO DO BOT AO TELEGRAM, O INPUT DEIXA DE SER A FRASE QUE O USUARIO IRA DIZER AO BOT, LOGO ESSE INPUT SE TORNA 'NONE' PARA SE TORNAR OPCIONAL, PARA PODER SER UTILIZADO EM OUTRA PLATAFORMA OU NAO
            frase = input('>: ')
        frase = str(frase)
        if 'executa ' in frase:
            return frase 
        frase = frase.lower()
        frase = frase.replace('é', 'eh')
        return frase

    def pensa(self, frase):
        if frase in self.frases: # PROCUROU NO DICIONARIO SE A FRASE QUE O USUARIO DIGITOU ESTAVA PRESENTE NO DICIONARIO
            return self.frases[frase] # RETORNA RESPOSTA PARA A FRASE
        elif frase == 'aprende': # COMANDO PARA O BOT APRENDER UMA NOVA FRASE E SUA RESPECTIVA RESPOSTA
            return 'O que devo aprender? '
        elif frase == 'tchau':
            return 'tchau'

        # RESPONDE FRASES QUE DEPENDEM DO HISTORICO
        ultimaFrase = self.historico[-1]
        if ultimaFrase == 'Ola, qual o seu nome?':
            nome = self.pegaNome(frase)
            resp = self.respondeNome(nome)
            return resp
        if ultimaFrase == 'O que devo aprender? ':
            self.chave = frase
            return 'OK, e qual a solução para isso? '
        if ultimaFrase == 'OK, e qual a solução para isso? ':
            resp = frase
            self.frases[self.chave] = resp 
            self.gravaMemoria()
            return 'APRENDIDO'

        try:
            resp = str(eval(frase)) # INSERINDO COMANDO DENTRO DE OUTRO COMANDO
            return resp
        except:
            pass
        return 'Nao entendi'
    
    def pegaNome(self, nome): # TRANSFORMAR O NOME DO USUARIO EM UM FORMATO LEGIVEL PARA O BOT
        if 'o meu nome eh ' in nome:
            nome = nome[14: ]

        nome = nome.title()
        return nome

    def respondeNome(self, nome): # PESQUISAR NA LISTA DE NOMES SE EXISTE OU NAO OP NOMEW DIGITADO
        if nome in self.conhecidos:
            frase = 'Eaew '
        else:
            frase = 'Muito prazer '
            self.conhecidos.append(nome) # ADICIONOU O NOME NA LISTA
            self.gravaMemoria()
        return frase+nome

    def gravaMemoria(self):
        memoria = open(self.nome + '.json', 'w') # ABRIU O ARQUIVO PARA ESCRITA
        json.dump([self.conhecidos, self.frases], memoria) # ESCREVEU OS NOMES DA LISTA DENTRO DO ARQUIVO DE MEMORIA DO CHATBOT
        memoria.close()

    def fala(self, frase): # RESPOSTA DO BOT PARA O USUARIO
        if 'executa ' in frase:
            plataforma = sys.platform
            comando = frase.replace('executa ', '')
            if 'win' in plataforma:
                os.startfile(comando)
            elif 'linux' in plataforma:
                try:
                    s.Popen(comando)
                except FileNotFoundError:
                    s.Popen(['xdg-open', comando])
        else:
            print(frase)
        self.historico.append(frase)
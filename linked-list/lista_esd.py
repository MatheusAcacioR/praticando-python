class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class Lista_Encadeada:
    def __init__(self):
        self.cabeca = None

    def inserir_no_inicio(self, dado):
        novo_no = No(dado)  # Cria um novo nó com o dado a ser armazenado

        if self.cabeca is None:  # Se a lista estiver vazia, define o dado a ser armazenado como o cabeça da lista
            self.cabeca = novo_no

            """Caso não esteja vazia, define o novo elemento como cabeça e o faz
            apontar para o antigo cabeça, que por fim vira o segundo elemento da lista"""
        else:
            novo_no.proximo = self.cabeca
            self.cabeca = novo_no

    def inserir_no_final(self, dado):
        novo_no = No(dado)  # Cria um novo nó com o dado a ser armazenado

        if self.cabeca is None:  # Se a lista estiver vazia, define o dado a ser armazenado como o cabeça da lista
            self.cabeca = novo_no
        else:  # Caso não esteja, percorre toda a lista para inserí-lo no final
            no_atual = self.cabeca
            while no_atual.proximo is not None:
                no_atual = no_atual.proximo
            no_atual.proximo = novo_no

    def remover_do_inicio(self):
        if self.cabeca is None:  # Caso a lista esteja vazia, retorna uma mensagem
            return "A fila está vazia!"
        else:  # Caso não esteja, remove o cabeça da lista, fazendo o segundo virar o primeiro da lista
            self.cabeca = self.cabeca.proximo

    def remover_do_final(self):
        if self.cabeca is None:  # Caso a lista esteja vazia, retorna uma mensagem
            return 'A fila está vazia!'
        elif self.cabeca.proximo is None:  # Caso tenha apenas 1 elemento, exclui o cabeça da lista
            self.cabeca = None
        else:  # Caso a lista possua mais de 1 elemento:
            no_atual = self.cabeca
            no_anterior = None

            while no_atual.proximo is not None:  # Enquanto o número depois do atual não for nulo:
                no_anterior = no_atual  # O nó atual vira o nó anterior
                no_atual = no_atual.proximo  # O nó seguinte vira o nó atual

            no_anterior.proximo = None  # Define o último nó como vazio

    def busca_sequencial(self, valor):  # Complexidade O(n)
        no_atual = self.cabeca
        while no_atual is not None:  # Percorre toda a lista até encontrar o elemento
            if no_atual.dado == valor:  # Verificando se algum item da lista é igual ao desejado
                return f"O valor {valor} está dentro da lista!"
            no_atual = no_atual.proximo  # Atualiza o nó atual
        return f"O valor {valor} não está dentro da lista!"  # O elemento não está na lista

    def bubble_sort(self, lista):       # Organiza a lista utilizando o algoritmo de ordenação Bubble Sort
        n = len(lista)
        for j in range(n - 1):
            for i in range(n - 1):
                if lista[i] > lista[i + 1]: 
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]


    def imprimir(self):
        no_atual = self.cabeca
        lista = []
        while no_atual is not None:         # Percorre a lista enquanto os elementos não forem vazios
            lista.append(no_atual.dado)
            no_atual = no_atual.proximo     # O próximo número da lista vira o atual
        return lista[0:len(lista)]

    def imprimir_bubble(self):
        no_atual = self.cabeca
        lista = []
        while no_atual is not None:         # Percorre a lista enquanto os elementos não forem vazios
            lista.append(no_atual.dado)
            no_atual = no_atual.proximo     # O próximo número da lista vira o atual
            self.bubble_sort(lista)         # Ordena os elementos utilizando o Bubble Sort
        return lista[0:len(lista)]



# -- TESTANDO AS FUNÇÕES

lista = Lista_Encadeada()

lista.inserir_no_inicio(10)
lista.inserir_no_inicio(30)  # Insere no início da lista os elementos 10, 30, 20, 40, 150, 360
lista.inserir_no_inicio(20)
lista.inserir_no_inicio(40)
lista.inserir_no_inicio(150)
lista.inserir_no_inicio(360)
print(lista.imprimir())

lista.remover_do_final()  # Remove o elemento que está no final da lista, no caso o número 10
print(lista.imprimir())

lista.remover_do_inicio()  # Remove o elemento que está no início da lista, no caso o número 360
print(lista.imprimir())

lista.inserir_no_final(90)      # Insere no final da lista o número 90
lista.inserir_no_inicio(120)    # Insere no início da lista o número 120
print(lista.imprimir())

print()
print(lista.busca_sequencial(30))   # Confere se o número 30 está na lista
print(lista.busca_sequencial(100))  # Confere se o número 100 está na lista
print()

print(lista.imprimir_bubble())      # Imprime os valores com o bubble sort






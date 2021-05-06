class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # Percorre todos os elementos da lista - Complexidade O(n)
    def append(self, elem):
        if self.head:
            # inserção quando a lista ja possui elemento
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            # primeira inserção
            self.head = Node(elem)
        self.size = self.size + 1

    # Atribui a função len do python para a classe e retornar o tamanho da lista
    def __len__(self):
        return self.size

    def _getNode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("List indes out of range")
        return pointer

    def __getitem__(self, index):
        pointer = self._getNode(index)
        if pointer:
            return pointer.data
        else: 
            raise IndexError("List indes out of range")

    def __setitem__(self, index, elem):
        pointer = self._getNode(index)
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("List indeX out of range")

    # Retorna o indice do elemento na lista
    def index(self, elem):
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i += 1
        raise ValueError(f'{elem} is not in list')

    # Inserção de um elemento em um local especifico da lista
    # Percorre todos os elementos da lista - Pior caso complexidade: O(1)
    def insert(self, index, elem):
        # Caso o usuario queira inserir o elemento no começo da lista
        node = Node(elem) # Elemento inserido na lista
        if index == 0:
            node.next = self.head # Como um novo elemento foi inserido no começo da lista e o elemento do começo da lista é a cabeça, o elemento que era a cabeça anteriormente passa a ser o proximo elemento
            self.head = node # O novo elemento inserido passa a ser a cabeça
        else:
            pointer = self._getNode(index - 1)
            """Ponteiro iniciando no começo da lista
            Verifica se o ponteiro não esta vazio (Cabeça pode estar vazia ou o index digitado 
            pode ser um numero maior que o tamanh da lista) e percorre até o elemento anterior 
            do index. Se o ponteiro não tiver vazio ele vai avançar pro próximo elemento
            """
            node.next = pointer.next
            pointer.next = node
            self.size = self.size + 1

    # Percorre todos os elementos da lista - Complexidade O(n)
    def remove(self, elem):
        if self.head == None:
            raise ValueError(f'{elem} is not in list')
        elif self.head.data == elem:
            self.head = self.head.next
            self.size = self.size - 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while(pointer):
                if pointer.data == elem:
                    #REMOVE
                    ancestor.next = pointer.next
                    pointer.next = None
                ancestor = pointer
                pointer = pointer.next
            return True
        raise ValueError(f'{elem} is not in list')

    def __repr__(self):
        r = ""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.data) + "-->"
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()
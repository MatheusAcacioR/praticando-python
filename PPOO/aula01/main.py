# Importando a classe molde de criação de uma pessoa
from pessoa import Pessoa

# Criando uma pessoa chamando a classe em uma variavel. Colocando os parametros na mesma ordem em que elas foram definidas na classe
p1 = Pessoa('Samantha', 20) # ESSA PESSOA SE CHAMA SAMANTHA, TEM 20 ANOS, NÃO ESTA COMENDO NEM FALANDO
p2 = Pessoa('Daniel', 18) # ESSA PESSOA SE CHAMA DANIEL, TEM 18 ANOS, NÃO ESTA COMENDO NEM FALANDO

print(p1.getBirthDate())
print(p2.getBirthDate())
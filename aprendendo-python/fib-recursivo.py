" Complexidade O(1) "

def fibonacci(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def contaFib(cont):
    print(f'{cont} primeiros termos da sequência de Fibonacci')
    for contador in range(0, cont + 1):
        if contador == 0:
            print(f'Fibonacci({contador}) = {contador}')
        else:
            print(f'Fibonacci({contador}) = {fibonacci(contador)}')

teste = contaFib(int(input('Quantos termos você quer contar?' )))

" Complexidade O(1) "

def fatorial(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    else:
        return n * fatorial(n - 1)


def contaFat(number):
    for c in range(0, number + 1):
        print(f'fatorial({c}) = {fatorial(c)}')

contaFat(int(input()))

"""if __name__ == "__main__":
    fatn = fatorial(n = int(input()))
    print(fatn)"""
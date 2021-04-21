from random import randint

a = [1, 2, 3, 4, 5]
i = 1

while i <= 10:
    b = int(randint(0, 4))
    print(a[b])
    i+=1
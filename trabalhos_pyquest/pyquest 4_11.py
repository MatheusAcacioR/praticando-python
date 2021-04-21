massa = 0.0
tempo = 0
massa = float(input("Massa: "))
while massa >= 0.5:
    massa = massa/2
    tempo = tempo + 50

print("A massa final foi {}g e demorou {} segundos para atingir seu tempo de meia-vida." .format(massa, tempo))
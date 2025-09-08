start = int(input("Digite o valor inicial: "))
step = int(input("Digite a PA: "))
timer = 10
valor = start
while timer != 0:
    print(f"{valor} ->", end=' ')
    valor +=step
    timer-=1
print("Fim")    
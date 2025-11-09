from random import randint
numero_maquina = 0
soma = 0
win = 0
choice = input("Digite 'p' para par e 'i' para impar: ").strip().lower()
while True:
    if choice == 'p':
        numero_jogador = int(input("Escolha um numero entre 1 e 10: "))
        numero_maquina = randint(1,11)
        soma = numero_maquina+numero_jogador
        if soma%2==0:
            win+=1
            print(f"Você ganhou, esta com a streak de {win} vitórias") 
        else:
            print(f"Perdeu... e sua streak de {win} zerou!")
            break

    elif choice == 'i':
        numero_jogador = int(input("Escolha um numero entre 1 e 10: "))
        numero_maquina = randint(1,11)
        soma = numero_maquina+numero_jogador
        if soma%2!=0:
            win+=1
            print(f"Você ganhou, esta com a streak de {win} vitórias") 
        else:
            print(f"Perdeu... e sua streak de {win} zerou!")
            break

    choice = input("Digite 'p' para par e 'i' para impar: ").strip().lower()    


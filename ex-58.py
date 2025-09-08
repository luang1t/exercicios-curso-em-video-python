from random import randint
cont = 1
numero_sortido = randint(0,10)
numero_escolhido = int(input("Digite um numero entre 1 e 10 se for o certo vc ganhou!\n1º Tentiva:\nDigite aqui: "))
while numero_escolhido is not numero_sortido:
    if numero_escolhido > numero_sortido:
        print("Dica: É um número menor.")
    else:
        print("Dica: É um número maior.")
    numero_escolhido = int(input(f"Digite um numero entre 1 e 10 se for o certo vc ganhou!\n{cont+1}º Tentiva:\nDigite aqui: "))    
    cont+=1
print(f"Ganhou com {cont} tentativas")
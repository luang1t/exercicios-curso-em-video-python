from random import randint
from time import sleep

numero = randint(1,5)
print("-=-"*20)
escolha = int(input("Tente descobrir um valor entre 1 e 5: "))
print("-=-"*20)
print("Processando...")
sleep(1)
while True:
    if escolha == numero:
        print("Processando...")
        sleep(1)
        print("Acertou")
        break
    else:
        print("Processando...")
        sleep(1)
        print("Errou")
    escolha = int(input("Tente novamente: "))
    print("Processando...")
    sleep(1)        
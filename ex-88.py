#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint

jogos = []
jogo = []
n_jogos = int(input("Digite o número de jogos desejado: "))
numeros = 0
for j in range(n_jogos):
    for i in range (6):
        numero =  randint(1,60)
        if numero not in jogo: 
            jogo.append(numero)
            
        else:
            while numero in jogo:
                numero = randint(1,61)
            jogo.append(numero)
                            
    jogos.append(jogo[:])
    jogo.clear()
print('=-'*30)
for i,jogo in enumerate(jogos):
    print(f"{i+1: 5^}º Jogo: {jogo}")
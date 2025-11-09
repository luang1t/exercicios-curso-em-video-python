import random

print("Suas opções: ")
print("[0] Pedra\n[1] Papel\n[2]Tesoura")
print("Qual a sua jogada?")
jogada = int(input("Digite aqui: "))
jogada_maquina = random.randint(0,2)
if jogada == 1 and jogada_maquina == 0:
    print("Parabéns, você ganhou!")
elif jogada == 0 and jogada_maquina == 1:
    print("Máquina wins")
elif jogada == 0 and jogada_maquina == 2:
    print("Parabéns você ganhou!")
elif jogada == 2 and jogada_maquina == 0:
    print("Máquina wins")
elif jogada == 1 and jogada_maquina == 2:
    print("Máquina wins")
elif jogada == 2 and jogada_maquina == 1:
    print("Parabéns você ganhou!")
else:
    print("empate")    
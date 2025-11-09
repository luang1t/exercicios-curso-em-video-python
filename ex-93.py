#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.


jogador = {}
gols_partida = []
gols_cont = 0
jogador['nome'] = input("Digite seu nome: ")
jogador['partidas'] = int(input("Digite o total de partidas jogadas nessa temporada: "))
for i in range(jogador['partidas']):
    gols = int(input(f"Digite quantos gols vc fez na {i+1}º partida: "))
    gols_partida.append(gols)

jogador['gols_p_partida'] = gols_partida[:]
jogador['total_gols'] = sum(gols_partida)
print(jogador)
print("ANALISE DO JOGADOR")
for k,v in jogador.items():
    print(f"{k} - {v}")


for i in range(len(jogador['gols_p_partida'])):
    print(f"=> Na partida {i+1} fez {jogador['gols_p_partida'][i]} gols")

print(f"O jogador {jogador['nome']} jogou {jogador['partidas']} partidas fazendo um total de {jogador['total_gols']} gols nessa temporada!")    
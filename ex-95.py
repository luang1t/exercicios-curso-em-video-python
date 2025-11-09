jogador = dict()
time = list()
gols = list()
total_gols = 0

while True:
    jogador.clear()

    jogador['nome'] = str(input("Digite o nome do jogador: "))
    jogador['partidas'] = int(input("Digite o numero de partidas jogadas: "))

    for data in range(jogador['partidas']):
        gol = int(input(f"Quantos gols na {data+1}º partida: "))
        gols.append(gol)
        total_gols+=gol

    jogador['gols'] = gols[:]
    jogador['total_gols'] = total_gols
    total_gols = 0
    gols.clear()
    time.append(jogador.copy())

    while True:
        valida = str(input("Deseja continuar: [S/N] ")).strip().upper()[0]

        if valida in 'SN':
            break
        else:
            print("Erro! Responda apenas 'S' ou 'N'.")

    if valida == 'N':
        break
print("-="*30)
for k,v in enumerate(time):
    print(f'{k:<4}', end = ' ')
    for d in v.values():
        print(f'{str(d):<15}', end = ' ')
    print()

while True:    
    select = int(input("Digite o indice do jogador que você deseja ver mais detalhes: (999 para parar)"))
    cont = 0
    if select == 999:
        break
    print(f"Levantamento do jogador {time[select]['nome']}")
    for i in time[select]['gols']:
        print(f"No jogo {cont+1} fez {i} gols")
        cont+=1
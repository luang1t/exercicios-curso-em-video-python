pessoas = []
dados = []
soma_peso = 0
while True:

    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Digite seu peso: ')))
    pessoas.append(dados[:])
    dados.clear()

    validacao = input('Deseja continuar?\n[S/N]: ').strip().lower()[0]
    if validacao == 's':
        continue
    elif validacao == 'n':
        break
    else:
        print('Tente novamente.')
        continue

for pessoa in range(len(pessoas)):
    soma_peso +=pessoas[pessoa][1]

media_peso = soma_peso/len(pessoas)

for pessoa in range(len(pessoas)):
    if pessoas[pessoa][1] > media_peso:
        print(f'{pessoas[pessoa][0]} está acima do peso com {pessoas[pessoa][1]}kg')
    else:
        print(f'{pessoas[pessoa][0]} está abaixo do peso com {pessoas[pessoa][1]}kg')  
        
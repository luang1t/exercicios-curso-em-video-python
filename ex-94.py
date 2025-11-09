#Programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média

pessoas = list()
pessoa = dict()
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Digite o seu nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Digite apenas F para feminino e M para masculino. Tente novamente')
    pessoa['idade'] = int(input("Digite a sua idade: "))
    soma+=pessoa['idade']
    pessoas.append(pessoa.copy())

    while True:
        valida = str(input('Deseja continuar cadastrando? [S/N] ')).upper().strip()[0]
        if valida in 'SN':
            break
        print("Erro! Responda apenas 'S' ou 'N'.")

    if valida == 'N':
        break

media = soma/len(pessoas)

print(f"-="*30)
print(f"Um total de {len(pessoas)} pessoas foram cadastradas.")
print(f"A média de idade é de {media:.0f} anos")

print(f"As mulheres cadastradas foram:")
for i in pessoas:
    if i['sexo'] == 'F':
        print(f"{i['nome']} ")
print()

print(f"Pessoas acima da média de idade: ")
for i in pessoas:
    if i['idade'] >= media:
        print("    ")
        for k,v in i.items():
            print(f"{k} = {v}; ")
        print()
print("Finished")       
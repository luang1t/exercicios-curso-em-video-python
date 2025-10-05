#Programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média

soma_idade = cont_m = cont_h = cont_bug = 0
pessoas_veias = list()
mulheres = list()
pessoas = list()
template = dict()

while True:

    template['nome'] = input("Digite seu nome ou 0 para sair: ")
    if template['nome'] == '0':
        break
    
    template['sexo'] = input("Digite 'H' para Homem ou 'M' para Mulher: ").strip().upper()[0]
    if template['sexo'] == 'H':
        template['idade'] = int(input("Digite sua idade: "))
        pessoas.append(template.copy())
        soma_idade+=template['idade']
        cont_h+=1
    elif template['sexo'] == 'M':
        template['idade'] = int(input("Digite sua idade: "))
        mulheres.append(template.copy())
        pessoas.append(template.copy())
        soma_idade+=template['idade']
        cont_m+=1
    else:
        print("Tente novamente. Digite algo relacionado com o que se pede!")
        cont_bug+=1
        continue
    
if pessoas:
    media = soma_idade/len(pessoas)
else:
    media = 0    

for pessoa in pessoas:
    for k,v in pessoa.items():
        print(f"{k}-{v}")

for pessoa in pessoas:
        if pessoa['idade'] > media:
            pessoas_veias.append(pessoa.copy())

print(f"O total de {len(pessoas)} pessoas foram cadastradas.")
print(f"A média de idade das pessoas cadastradas é de {media:.2f} anos.")
print(f"Lista de mulheres cadastradas:\n{[m['nome'] for m in mulheres]}")

print(f"As pessoas mais velhas encontradas: ")
for v in pessoas_veias:
    print(f"{v["nome"]} - ({v["idade"]} anos)")
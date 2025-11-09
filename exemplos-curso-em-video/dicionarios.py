pessoas = {
    'nome': 'Gustavo', 'sexo': 'M', 'idade': 22
}
del pessoas ['sexo']
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos e é do sexo {pessoas["sexo"]}.')
pessoas ['nome'] = 'Leandro'
pessoas ['peso'] = 98.5
print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())

for k,v in pessoas.items():
    print(f"{k} = {v}")
#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime

recolhe_dados = dict()

recolhe_dados['nome'] = input("Digite seu nome: ")
recolhe_dados['ano_nascimento'] = int(input("Em que ano você nasceu: "))
recolhe_dados['CTPS'] = int(input("Carteira de trabalho (0 não tem): "))
recolhe_dados['idade'] = 2025-recolhe_dados['ano_nascimento']

if recolhe_dados['CTPS']!=0:
    recolhe_dados['ano_contratação'] = int(input("Digite o ano de contratação: "))
    recolhe_dados['ano_aposentadoria'] = recolhe_dados['idade'] + ((recolhe_dados['ano_contratação']+35)-datetime.now().year)
    recolhe_dados['salario'] = float(input("Digite seu sálario R$: "))
print(recolhe_dados)

for k,v in recolhe_dados.items():
    print(f"- {k} tem o valor {v}")
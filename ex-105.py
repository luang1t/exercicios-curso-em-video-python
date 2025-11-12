#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#– Quantidade de notas   

#   – A maior nota                                                                                                                                                               
#       – A menor nota                                                                                                                                                              
#           – A média da turma                                                                                                                                                      
#               – A situação (opcional)
from random import randint

qtd_notas = int(input("Digite quantas notas vc quer gerar: "))

notas_cadastradas = list()

for _ in range(qtd_notas):
    notas_cadastradas.append(randint(0,10))



def notas_descricao(*notas_alunos):

    quantida_notas = len(notas_alunos)
    maior_nota = max(notas_alunos)
    menor_nota = min(notas_alunos)
    media_turma = sum(notas_alunos)/len(notas_alunos)

    return {'quantida_notas':quantida_notas,'maior':maior_nota,'menor':menor_nota,'media':media_turma}

descriacao = notas_descricao(*notas_cadastradas)

print(descriacao, notas_cadastradas)
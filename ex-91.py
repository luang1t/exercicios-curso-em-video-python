#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter

resultados = {
    'primeiro':randint(1,6),
    'segundo':randint(1,6),
    'terceiro':randint(1,6),
    'quarto':randint(1,6)
}
melhores_resultados = list()

print("Valores sorteados: ")
for k,v in resultados.items():
    print(f"{k} - {v}")
    sleep(1)

melhores_resultados = sorted(resultados.items(), key = itemgetter(1), reverse=True)
print(melhores_resultados)
#itemgetter(1) pega apenas o valor
#itemgetter(0) pega apenas a chave
#é necessário criar outro dicionario para deixar em ordem, no caso criei o dicionario 'melhores_resultdos' para armazenar nossos valores ordenados
#utilizando o reverse = true para deixar do maior para o menor
#sorted(resultados.items(), key = itemgetter(1))

for i,v in enumerate(melhores_resultados):
    print(f"{i+1}º lugar: {v[0]} com {v[1]}.")
    sleep(0.5)
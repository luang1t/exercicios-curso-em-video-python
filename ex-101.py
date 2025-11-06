#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
from datetime import datetime


def voto_situacao(ano_nascimento):
    idade = (datetime.now().year) - ano_nascimento
    if idade >= 65:
        return f"Idade: {idade} anos\nVoto - Opcional"
    elif 18 <= idade < 65:
        return f"Idade: {idade} anos\nVoto - Obrigatório"
    elif idade >= 16:
        return f"Idade: {idade} anos\nVoto - Opcional"
    else:
        return f"Idade: {idade} anos\nVoto - Negado"
    
    
consulta = int(input("Digite o seu ano de nascimento para saber se você está apto para votar: "))
print(voto_situacao(consulta))
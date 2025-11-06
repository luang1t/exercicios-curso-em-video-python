#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
from datetime import date


def voto_situacao(ano_nascimento):
    idade = date.today().year - ano_nascimento
    if idade < 16:
        return f"Idade: {idade} anos\nVoto - Negado"
    elif 16 <= idade < 18 or idade > 65:
        return f"Idade: {idade} anos\nVoto - Opcional"
    else:
        return f"Idade: {idade} anos\nVoto - Obrigatório"
    
    
consulta = int(input("Digite o seu ano de nascimento para saber se você está apto para votar: "))
print(voto_situacao(consulta))
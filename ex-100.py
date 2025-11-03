#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep


numeros = []

def sorteia(list):
    print('Sorteando os valores na lista: ', end='')
    for _ in range(0,5):
        numero = randint(1,10)
        numeros.append(numero)
        print(f'{numero} ', end='', flush = True)
        sleep(0.3)
    print('Pronto!')    
def somaPar(list):
    soma = 0
    for numero in list:
        if numero % 2 == 0:
            soma+=numero
    print(f'Somando os valores pares de {list}, temos {soma}')

sorteia(numeros)
somaPar(numeros)
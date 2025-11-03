#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint

numeros = []

def sorteia(cont):
    for _ in range(cont):
        numero = randint(0,10)
        numeros.append(numero)
def somaPar():
    soma = 0
    for _ in range(len(numeros)):
        if numeros[_]%2==0:
            soma+=numeros[_]
    return soma    

vezes = int(input("Digite quantas vezes: "))

sorteia(vezes)
print(numeros)
print(somaPar())


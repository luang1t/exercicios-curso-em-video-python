#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que 
# indique o número a calcular e outro chamado show, que será um valor lógico (opcional) 
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
from time import sleep

def fatorial(num):
    resultado = 1
    print(f"{num}! = ",end= '')
    for fat in range(num,0,-1):
        print(f"{fat}x ", end = '',flush=True)
        sleep(0.3)
        resultado *= fat
    return resultado

solicita = int(input("Digite um numero para saber seu fatorial: "))
print(f" = {fatorial(solicita)}") 
#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que 
# indique o número a calcular e outro chamado show, que será um valor lógico (opcional) 
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
from time import sleep

def fatorial(num,show=False):
    """
    --> Calcula fatoial de um número.
    :param num: Número a ser calcula o fatorial.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número num.
    """
    resultado = 1
    
    for fat in range(num,0,-1):
        if show:
            print(f"{num}! = ",end= '')
            if fat > 1:
                print(f"{fat}x ", end = '',flush=True)
                sleep(0.3)
            else:
                print(f"{fat}x ", end = '',flush=True)    
        resultado *= fat
    return resultado

solicita = int(input("Digite um numero para saber seu fatorial: "))
print(f" = {fatorial(solicita,show=True)}") 
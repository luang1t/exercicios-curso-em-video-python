#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

from moeda import *

valor_user = float(input("Digite um valor R$:"))

print(f"R$: {valor_user} aumentado em 10% é R$: {aumentar(valor_user,10)}")
print(f"R$: {valor_user} diminuido em 10% é R$: {diminuir(valor_user,10)}")
print(f"R$: {valor_user} dobrado R$: {dobro(valor_user)}")
print(f"R$: {valor_user} pela metade fica R$: {metade(valor_user)}")
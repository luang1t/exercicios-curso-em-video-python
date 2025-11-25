#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

from moeda import *

valor_user = float(input("Digite um valor R$:"))


print(f"""
{conversor(valor_user)} acrescentado em 10% é  {conversor(aumentar(valor_user,10))}
{conversor(valor_user)} diminuindo em 10% é {conversor(diminuir(valor_user,10))}
{conversor(valor_user)} dobrado fica {conversor(dobro(valor_user))}
{conversor(valor_user)} pela metado fica {conversor(metade(valor_user))}
""")
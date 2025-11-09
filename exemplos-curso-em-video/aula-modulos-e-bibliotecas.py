#IMPORTANDO TODAS AS FUNÇÕES EXISTENTES NA BIBLIOTECA
import math

num = int (input("Digite um numero: "))
raiz = math.sqrt(num)
print(f"A raiz de {num} é {math.ceil(raiz)} arredondado para cima.")
print(f"A raiz de {num} é {math.floor(raiz)} arredondado para baixo.")
print(f"A raiz de {num} em sua porção inteira é {math.trunc(raiz)}")


#IMPORTANDO FUNÇÕES ESPECIFICAS DA BIBLIOTECA
from math import sqrt,ceil,floor

numero = int(input("Digite um número: "))
raiz = sqrt(numero)
print(f"A raiz quadrada de {numero} é {raiz}")
print(f"A raiz quadrada de {numero} arredondada para cima é {ceil(raiz)}")
print(f"A raiz quadrada de {numero} arredondada para baixo é {floor(raiz)}")

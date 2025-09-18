from random import randint

numeros = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
for numero in numeros:
    print(numero)
    
print(f"Lista dos 5 números gerados aleatoriamente: {numeros}.\nO maior número gerado foi: {max(numeros)}.\nO menor número gerado: {min(numeros)}.")    
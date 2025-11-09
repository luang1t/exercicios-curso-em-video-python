numero = cont = soma = 0

numero = int(input("Digite um numero ou 999 para sair: "))
while numero != 999:
    soma += numero
    cont+=1
    numero = int(input("Digite um numero ou 999 para sair: "))
print(soma,cont)    

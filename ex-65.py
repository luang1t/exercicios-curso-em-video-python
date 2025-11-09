soma = 0
cont=0
valores = int(input("Digite um valor ou 0 para sair e ver a média entre todos os valores e qual foi o maior e o menor valore: "))
while valores != 0:
    if cont == 0:
        maior_valor = valores
        menor_valor = valores

    if valores > maior_valor:
        maior_valor = valores

    elif valores < menor_valor:
        menor_valor = valores 

    soma+=valores
    cont+=1
    
    valores = int(input("Digite um valor para continuar somando ou 0 para sair e ver a média entre todos os valores e qual foi o maior e o menor valore: "))
print(f"media dos valores: {soma/cont}\nsoma dos resultados: {soma}\nmaior valor: {maior_valor}\nmenor valor: {menor_valor}")    
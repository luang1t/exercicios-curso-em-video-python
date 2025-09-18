qtd_itens = int(input("Quantos itens tem no seu carrinho: "))
primeiro = qtd_itens
total_goasto = 0
maior_mil = 0
maior = 0
while primeiro > 0:
    nome_item = input("Digite o nome do item: ")
    preco_item = float(input("Digite o valor do item: "))
    if primeiro == qtd_itens:
        maior = preco_item
    if preco_item > maior:
        maior = nome_item  
    total_goasto+=preco_item
    if preco_item>1000:
        maior_mil+=1
    primeiro-=1
print(maior,total_goasto,maior_mil)


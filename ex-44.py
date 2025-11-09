import os
def clear():
    os.system("cls")

def recebe_preco():
    while True:
        try:
            preco_produto = int(input("digite o valor do produto: \nR$:"))
            return preco_produto
        except ValueError:
            print("Digite algo no contexto do programa.")

valor_produto = recebe_preco()
seletor = int(input("1 - À vista dinheiro/cheque\n2 - À vista no cartão\n3 - Em até duas vezes no cartão\n4 - 3x ou mais\nDigite aqui:"))
if seletor == 1:
    novo_valor = valor_produto-(valor_produto*0.1)
    print(f"valor a pagar à vista no cartão ou cheque R$:{novo_valor}")
elif seletor == 2:
    novo_valor = valor_produto-(valor_produto*0.05)
    print(f"valor a pagar à vista no cartão R$:{novo_valor}")
elif seletor == 3:
    print(f"valor a pagar em 2x {valor_produto/2}")
elif seletor == 4:
    novo_valor = valor_produto+(valor_produto*0.3)
    print(f"valor a pagar em 3x com juros de 20% R$:{novo_valor}")
else:
    print("Digite uma opção do menu.")
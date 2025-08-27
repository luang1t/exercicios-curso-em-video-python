dinheiro = float(input("Digite quanto de dinheiro tem na carteira: "))
um_dol = 3.27
conversao = dinheiro/um_dol
print(f"Você tem R$:{dinheiro:.2f}\nCom o valor do dolar atual em R$3.27 é possivel adquirir US$:{(dinheiro/um_dol):.2f}")
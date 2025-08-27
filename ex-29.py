velocidade = float(input("Digite sua velocidade em Km/H: "))
if velocidade > 80:
    print("Multa aplicada!")
    print(f"Valor a pagar R$:{(velocidade-80)*7:.2f}")
else:
    print("Limite permitido, boa viagem!")    
salario = input("Digite seu salario: ")

if int(salario) < 1250:
    novo_salario = int(salario)+(int(salario)*0.15)
    print(f"Novo salario R$:{novo_salario} com aint(umento )de R$:{int(salario)*0.15}")
else:
    novo_salario = int(salario)+(int(salario)*0.1)
    print(f"Novo salario R$:{novo_salario} com aumento de R$:{int(salario)*0.1}")
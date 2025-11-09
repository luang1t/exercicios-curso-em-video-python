idade_h_velho = 0
nome_h_velho = ''
soma_m_menor_vint = 0
soma_idade = 0

for i in range (1,5):
    sexo = input("Digite 'M' para mulher e 'H' para homem: ").title().strip()
    if sexo == 'H':
        nome = input("Digite seu nome: ").title().strip()
        idade = int(input("Digite sua idade: "))
        soma_idade += idade
        if idade > idade_h_velho:
            idade_h_velho = idade
            nome_h_velho = nome
    elif sexo == 'M':
        nome = input("Digite seu nome: ").title().strip()
        idade = int(input("Digite sua idade: "))
        if idade < 20:
            soma_m_menor_vint += 1
        soma_idade += idade    

media = soma_idade/4
print(f"Média de idade é de {media} anos e o homem mais velho é o {nome_h_velho} com {idade_h_velho} anos e temos {soma_m_menor_vint} mulheres com menos de 20 anos.")

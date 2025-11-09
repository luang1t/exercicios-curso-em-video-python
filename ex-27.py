nome = input("Digite seu nome: ").strip()

nome_splitado = nome.split()
print(f"Primeiro nome: {nome_splitado[0]}")
print(f"Sobrenome: {nome_splitado[-1]}")
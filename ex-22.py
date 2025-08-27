nome = input("Digite seu nome completo: ").strip()
print(f"Nome em caixa alta: {nome.upper()}")
print(f"Nome em caixa baixa: {nome.lower()}")
print(f"Seu nome tem {nome.count(" ")} espaços")
print(f"O seu nome tem {(len(nome) - nome.count(" "))} letras")



nome_splitado = nome.split()
primeiro_nome = nome_splitado[0]
print(f"Seu primeio nome é {primeiro_nome} ele tem {len(primeiro_nome)} letras")
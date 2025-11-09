nome_cidade = input("Digite o nome da cidade: ").strip()

print(f"Se printar 0 é pq o nome da cidade começa com Santo: {nome_cidade.lower().find("santo")}")
print(nome_cidade[:5].upper() == "SANTO")
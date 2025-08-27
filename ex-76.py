produtos = (
    "Arroz", 25.50,
    "Feijão", 12.30,
    "Macarrão", 8.90,
    "Leite", 5.20,
    "Ovos", 14.00
)

for i in range(0,len(produtos),2):
    print(f"{produtos[i]}----------------{produtos[i+1]}")
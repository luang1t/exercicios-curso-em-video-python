brasileirao_2025 = (
    "Flamengo",
    "Palmeiras",
    "Cruzeiro",
    "Bahia",
    "Botafogo",
    "Mirassol",
    "São Paulo",
    "Fluminense",
    "Red Bull Bragantino",
    "Ceará",
    "Atlético Mineiro",
    "Internacional",
    "Grêmio",
    "Corinthians",
    "Santos",
    "Vasco da Gama",
    "Vitória",
    "Juventude",
    "Fortaleza",
    "Sport"
)
print(brasileirao_2025[0:5])
print(brasileirao_2025[-4:])
print(sorted(brasileirao_2025))

for i in range(len(brasileirao_2025)):
    if brasileirao_2025[i] == 'Corinthians':
        print(f"O {brasileirao_2025[i]} está em {i+1}º da tabela!")
        break
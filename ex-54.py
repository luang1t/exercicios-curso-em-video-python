lista_ano = []

for i in range(7):
    ano = int(input("Digite o ano."))
    lista_ano.append(ano)

soma = 0
for i in range(len(lista_ano)):
    if 2025-lista_ano[i]!=18:
        soma+=1

print(soma)        
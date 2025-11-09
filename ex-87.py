matriz = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
soma_ter_colu = 0
soma_pares = 0
menor_valor = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f"Digite o numero para a linha {linha}-{coluna}: "))

for linha in range(0,3):
    for coluna in range(0,3):
        if linha == 2 and coluna == 0:
            menor_valor = matriz[linha][coluna]
        if matriz[linha][coluna]<menor_valor:
            menor_valor = matriz[linha][coluna]
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
        print(f"[{matriz[linha][coluna]:^5}]", end = "")
    print()  

print(f"A soma de todos os numeros pares é {soma_pares}")
print(f"Soma dos elementos da terceira coluna {soma_ter_colu}")
print(f"O menor valor da segunda linha é {menor_valor}")

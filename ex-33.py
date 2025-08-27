numeros = []

for numero in range(3):
    numero = int(input(f"Digite o {numero+1} numero: "))
    numeros.append(numero)

posicao = sorted(numeros)
print(f"O maior numero é: {posicao[2]}")
print(f"O menor numero é: {posicao[0]}")

numeros = []
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)
print(f'O maior número é o {max(numeros)}')
print(f'O menor número é o {min(numeros)}')    
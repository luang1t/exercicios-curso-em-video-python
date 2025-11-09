numeros = []
numeros_pares = []
numeros_impares = []

while True:
    numero = float(input("Digite um numero: "))
    numeros.append(numero)
    validacao = input("Deseja continuar?\n[S/N]: ").strip().lower()[0]
    if validacao == 's':
        continue
    elif validacao == 'n':
        break

for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
    elif numero % 2 !=0:
        numeros_impares.append(numero)

print(numeros)
print(numeros_pares)
print(numeros_impares)
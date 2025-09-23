numeros = []

while True:

    numero = int(input("Digite um numero¹: "))
    numeros.append(numero)
    continuar = input("Deseja continuar?\n[S/N]: ").strip().lower()[0]

    if continuar == 's':
        continue
    elif continuar == 'n':
        break

print(len(numeros))
numeros.sort(reverse=True)
print(numeros)

if 5 in numeros:
    print("Número 5 está na lista")
else:
    print("Não tem número 5 na lista") 
    
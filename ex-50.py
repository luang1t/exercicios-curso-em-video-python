numeros = []
for numero in range(6):
    numero = int(input(f"Digite {numero+1} numero: "))
    numeros.append(numero)
print(numeros)

soma = 0
for i in numeros:
    if i % 2 == 0:
        soma+=i
print(soma)        
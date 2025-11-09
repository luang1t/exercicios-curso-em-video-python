numeros = []

for i in range(0,5):
    numero = int(input("Digite um valor: "))
    if i == 0 or numero > numeros[-1]:
        numeros.append(numero)
        print(f'Valor adicionado ao final da fila...')
    else:
        pos = 0
        while pos < len(numeros):
            if numero <= numeros[pos]:
                numeros.insert(pos,numero)
                print(f'{numero} adicionado na posição {pos}')
                break
            pos+=1
print(numeros)
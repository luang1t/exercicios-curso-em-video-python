numero_1 = int(input("Digite o primeiro numero: "))
numero_2 = int(input("Digite o segundo numero: "))
numero_3 = int(input("Digite o terceiro numero: "))
numero_4 = int(input("Digite o quatro numero: "))
achou = False
cont_9 = 0
numeros = (numero_1,numero_2,numero_3,numero_4)
for i in numeros:
    if i%2==0:
        print(f"{i}", end=" ")
for i in numeros:
    if i == 3 and achou == False:
        achou = True
        print(f"O numero 3 aparece primeiro na posição {numeros.index(i)+1}")
    if i == 9:
        cont_9+=1
print(cont_9)

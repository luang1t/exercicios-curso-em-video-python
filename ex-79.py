numeros = []
numero = int(input("Digite um número ou -1 para finalizar o programa: "))
while True:
    if numero == -1:
        numeros.sort()
        print(f"{numeros}")
        break
    else:
        if numero in numeros:
            numero = int(input("Número ja foi inserido digite outro ou -1 para finalizar o programa: "))
        else:
            numeros.append(numero)
            print("Número cadastrado!")
    numero = int(input("Digite um número ou -1 para finalizar o programa²: "))        
soma = cont = 0
numero = int(input("Digite um numero para somar se quiser sair digite 999 e verá o resultado soma: "))
while True:
    if numero == 999:
        break
    else:
        soma+=numero
        cont+=1
        numero = int(input("Digite um numero para somar se quiser sair digite 999 e verá o resultado da soma: "))
print(soma)
print(cont)        
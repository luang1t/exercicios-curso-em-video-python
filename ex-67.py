numero = int(input("Digite um numero para saber sua tabuada, ou um numero negativo para finalizar: "))
while True:
    if numero<0:
        break
    else:
        for i in range(1,11):
            print(f"{numero}*{i}={numero*i}")
        numero = int(input("Digite o proximo numero para saber sua tabuada, ou um numero negativo para finalizar: "))  

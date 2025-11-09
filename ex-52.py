while True:
    soma = 0
    primo = int(input("Digite um numero para saber se ele é primo:"))
    for i in range(1,primo+1):
        if primo % i == 0:
            soma+=1
    print(soma)
    if primo == 0:
        break
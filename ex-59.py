valores = []
for i in range(2):
        valor = float(input(f"Digite o {i+1}º valor: "))
        valores.append(valor)
while True:
    seletor = int(input("""Escolha uma das opções: 
[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa
                        
Digite aqui:                         
"""))
    if seletor == 1:
        print(sum(valores))
    elif seletor == 2:
        print(valores[0]*valores[1])
    elif seletor == 3:
        print(max(valores))    
    elif seletor == 4:
        valores[0] = float(input("Digite o novo primeiro valor: "))
        valores[1] = float(input("Digite o novo segundo valor: "))
        print(valores[0])
        print(valores[1])
    elif seletor == 5:
        break
    else:
        print("Digite algo no contexto do programa.")
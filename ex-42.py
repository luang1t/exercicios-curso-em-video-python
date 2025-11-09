def verificar_lados():
    while True:
        lados = []
        try:
            for i in range (3):
                lado = float(input(f"Digite um {i+1} lado: "))
                if lado > 0:
                    lados.append(lado)
                else:
                    print("O lado tem que ser maior que zero.")
                    
                    break
        except ValueError:
                print("Digite números apenas.")
                
        if len(lados) == 3:
            return lados
        
lados = verificar_lados()

a,b,c = lados
if (a + b > c) and (a + c > b) and (b + c > a):
    triangulo = "triângulo"
    if (a == b == c):
        print("Equilatero")
    elif ( (a == b and a != c) or (a == c and a != b) or (b == c and b != a) ):
        print(f"É um {triangulo} Isósceles")
    else:
        print(f"É um {triangulo} Escaleno")
else:
    print("Lista Vazia")
def verificar_lados():
    lados = []
    while True:
        try:
            for i in range (3):
                lado = float(input(f"Digite um {i+1} lado: "))
                if lado > 0:
                    lados.append(lado)
                else:
                    print("O lado tem que ser maior que zero.")
                    lados.clear()
                    break
        except ValueError:
                print("Digite números apenas.")
                lados.clear()
        if len(lados) == 3:
            return lados
            break
        
lados = verificar_lados()
if lados:
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
    print("Não é triangulo")
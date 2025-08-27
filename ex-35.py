lado_a = float(input("Digite um lado: "))
lado_b = float(input("Digite um lado: "))
lado_c = float(input("Digite um lado: "))

if (lado_a+lado_b)>lado_c and (lado_a+lado_c)>lado_b and (lado_b+lado_c)>lado_a:
    print("É triangulo")   
else:
    print("Não é triangulo")    
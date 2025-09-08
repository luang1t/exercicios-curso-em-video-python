start = int(input("Valor inicial: "))
step = int(input("Progressão aritimética: "))
progressao_a = start
while True:
    select = int(input("""[1] - P.A
[2] - Novos valores
[0] - Fim
Digite aqui: """))
    if select == 1:
        timer = 0
        progressao_a = start
        while timer != 10:
            print(f"{progressao_a}->", end=' ')
            progressao_a+=step
            if timer == 9:
                select = int(input("""\nDeseja contar mais?
[1] - Sim
[0] - Não
Digite aqui: """))
                if select == 1:
                    mais_valores = int(input("Digite quantas vezes vc quer mais: "))
                    timer = timer - mais_valores
                elif select == 0:
                    break
                else:
                    print("Digite algo correspondente ao programa")
                    continue     
            timer+=1
        print("Fim")
    elif select == 2:
        start = int(input("Menu - Valor inicial: "))
        step = int(input("Menu - Progressão aritimética: "))
    elif select == 0:
        break
    else:
        print("Digite algo correspondente ao programa: ") 
        continue   
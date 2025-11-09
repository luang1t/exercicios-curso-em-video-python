import random
primeiro = input("Digite o nome do primeiro aluno")
segundo = input("Digite o nome do segundo aluno")
terceiro = input("Digite o nome do terceiro aluno")
quarto = input("Digite o nome do quarto aluno")
sorteado = 0
sorteado_um = False
sorteado_dois = False
sorteado_tres = False
sorteado_quatro = False
while True:    
        sorteio = random.randint(1,4)
        if sorteio == 1:
            if sorteado_um == False:
                print(primeiro)
                sorteado_um = True
                sorteado+=1
        elif sorteio == 2:
            if sorteado_dois == False:
                print(segundo)
                sorteado_dois = True
                sorteado+=1
        elif sorteio == 3:
            if sorteado_tres == False:
                print(terceiro)
                sorteado_tres = True
                sorteado+=1
        else:
            if sorteado_quatro == False:
                print(quarto)
                sorteado_quatro = True
                sorteado+=1
        if sorteado == 4 and sorteado_um == True and sorteado_dois == True and sorteado_tres == True and sorteado_quatro == True  :
             break    

            
           
                


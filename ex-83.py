expressao = input("Digite uma expressão matematica com parenteses: ")
aberto = 0
correto = True

for caract in expressao:
    if caract == '(':
        aberto += 1

    elif caract == ')':

        if aberto > 0:
            aberto -= 1  

        else:
            correto = False
            break

if correto and aberto == 0:
    print("Operação correta")

else:
    print("Operação incorreta")    
import os
def clear():
    os.system('cls')
def recolhe_idade():
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if idade > 0:
                return idade
            else:
                print("Digite uma idade maior que zero kkk")
        except ValueError:
            clear()
            print("Digite algo no contexto do programa.")

idade = recolhe_idade()

print(idade)
if idade <=9:
    print("Mirim")
elif idade <= 14:
    print("Infantil")
elif idade <= 19:
    print("Júnior")
elif idade <= 25:
    print("Sênior")
else:
    print("Master")                                   
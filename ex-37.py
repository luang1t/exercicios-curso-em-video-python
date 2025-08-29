import os
def clear():
    return os.system('cls')

def exibir_menu():
    return print("""        MENU CONVERSOR
                 
1 - Converter para binário:
2 - Converter para Hexadecimal
3 - Converter para Octadecimal                               
""")

def recolher_numero():
    while True:    
        try:
            numero = int(input("Digite um número para saber sua conversão: "))
            return numero
        except ValueError:
            print("Digite apenas numeros.")
        

numero = recolher_numero()
clear()

while True:
    clear()
    exibir_menu()
    try:
        seletor = int(input("Digite aqui: "))
        if seletor == 1:
            print(bin(numero))
            break
        elif seletor == 2:
            print(hex(numero))
            break
        elif seletor == 3:
            print == (oct(numero))
            break
        else:
            clear()
            print("Código inválido, digite algo válido no contexto do menu.") 
    except ValueError:
        clear()
        print("Digite algo válido no contexto do menu.")

            
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
            clear()
            print("Digite apenas numeros.")
            
        
while True:
    exibir_menu()
    try:
            seletor = int(input("Digite aqui: "))
            if seletor == 1:
                numero = recolher_numero()
                clear()
                print(f"{numero} em binario {bin(numero)}")
            elif seletor == 2:
                numero = recolher_numero()
                clear()
                print(f"{numero} em hexadecial {hex(numero)}")
            elif seletor == 3:
                numero = recolher_numero()
                clear()
                print == (f"{numero} em octadecial {oct(numero)}")
            else:
                clear()
                print("Código inválido, digite algo válido no contexto do menu.") 
    except ValueError:
            clear()
            print("Digite algo válido no contexto do menu.")

            
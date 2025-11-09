import os
def clear(): 
    return os.system('cls')
def recolher_dados():
    while True:
        clear()
        dados = {"valor_casa": "", "salario": "", "anos_pagar" : ""}
        try:
            for chave in dados:
                if chave == "anos_pagar":
                    valor = int(input(f"Digite {chave}: "))    
                else:    
                    valor = float(input(f"Digite {chave}: "))
                dados[chave] = valor
            return dados
        except ValueError:
            clear()
            print("Erro de digitação identificado, tente novamente.")        

dados_cliente = recolher_dados()

porcentagem_validacao = dados_cliente["salario"] * 0.3

meses = dados_cliente["anos_pagar"] * 12

prestacao = dados_cliente["valor_casa"]/meses

clear()
if prestacao > porcentagem_validacao:
    print(f"""Emprestimo NEGADO!
Motivo: para ser aprovado é necessário que a prestação seja menor que 30% do seu salário!
Sua situação atual é:
30% do seu salário R${porcentagem_validacao:.2f}
Prestação R$:{prestacao:.2f}""")
else:
    print(f"""Emprestimo APROVADO!
Prestação R$:{prestacao:.2f}
Meses: {meses}""")    
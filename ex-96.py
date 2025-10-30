def area(largura,comprimento):
    area_terreno = largura*comprimento
    print(f"A área de um terreno com largura {largura}m por {comprimento}m de compriemento é de {area_terreno}.")

def design_line():
    print("-"*30)

def mensagem(msg):
    print(msg)
    
mensagem('Controle de terrenos')
design_line()
largura = float(input("LARGURA (m): "))
design_line()
comprimento = float(input("COMPRIMENTO (m): "))
design_line()
area(largura,comprimento)
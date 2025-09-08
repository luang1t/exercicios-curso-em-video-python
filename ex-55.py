lista_pesos = []
peso_maior = 0
peso_menor = 0
for i in range (1,6):
    pessoas = float(input(f"Digite o peso da {i} pessoa: "))
    lista_pesos.append(pessoas)
    if i == 1:
        peso_maior = pessoas
        peso_menor = pessoas
    else:
        if pessoas > peso_maior:
            peso_maior = pessoas
        elif pessoas < peso_menor:
            peso_menor = pessoas        
        


print(peso_maior)
print(peso_menor)
print(max(lista_pesos))  
print(min(lista_pesos))  

saque = int(input("Digite o valor do saque: "))
decremento = saque
notas_cinquenta=0
notas_vinte=0
notas_dez=0
notas_um = 0

while True:
    if saque >= 50:
        notas_cinquenta = saque // 50
        decremento = saque % 50
        if decremento >= 20:
            notas_vinte = decremento // 20
            decremento = decremento % 20
        if decremento >= 10:
            notas_dez = decremento // 10
            decremento = decremento % 10
        if decremento >= 1:
            notas_um = decremento // 1
            decremento = decremento % 1
        if decremento == 0:
            break     
    elif saque >= 20:        
        notas_vinte = decremento // 20
        decremento = decremento % 20
        if decremento >= 10:
            notas_dez = decremento // 10
            decremento = decremento % 10
        if decremento >= 1:
            notas_um = decremento // 1
            decremento = decremento % 1
        if decremento == 0:
            break 
    elif saque >= 10:        
        notas_dez = decremento // 10
        decremento = decremento % 10
        if decremento >= 1:
            notas_um = decremento // 1
            decremento = decremento % 1
        if decremento == 0:
            break
    elif saque >= 1:        
        notas_um = decremento // 1
        decremento = decremento % 1       
        if decremento == 0:
            break
print(f"notas de 50: {notas_cinquenta}\nnotas de 20: {notas_vinte}\nnotas de 10: {notas_dez}\nnotas de 1: {notas_um}")
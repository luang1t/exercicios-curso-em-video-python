maior_de_idade = 0
mulheres_menos_vinte = 0
homens = 0
sexo = input("Digite seu sexo:\n[F] - Femea\n[M] - Macho").strip().upper()
while True:
    if sexo == 'F':
        idade = int(input("Digite sua idade: "))
        if idade > 18:
            maior_de_idade+=1
        if idade < 20:
            mulheres_menos_vinte+=1
    elif sexo == 'M':
        idade = int(input("Digite sua idade: "))
        if idade > 18:
            maior_de_idade+=1
        homens+=1
    select  = input("Deseja cadastrar mais:\n[S] - Sim\n[N] - Não\nDigite aqui: ") 
    if select == 'S':
        sexo = input("Digite seu sexo:\n[F] - Femea\n[M] - Macho").strip().upper()
    elif select =='N':
        break
print(maior_de_idade)
print(mulheres_menos_vinte)
print(homens)        
                 


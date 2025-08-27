ano = (input("Digite o ano para saber se ele é bisexto ou 0 para saber do ano atual: "))

if ano == '0':
    ano_atual = '2025'
    if ano_atual [2:] == '00' and int(ano_atual) % 400 == 0:
        print("Bisexto")
    elif int(ano_atual) % 4 == 0 and ano_atual [2:] != '00':
        print("Bisexto")
    else:
        print("Não é bisexto")
else:
    if ano [2:] == '00' and int(ano) % 400 == 0:
        print("Bisexto")
    elif int(ano) % 4 == 0 and ano [2:] != '00':
        print("Bisexto")
    else:
        print("Não é bisexto")    
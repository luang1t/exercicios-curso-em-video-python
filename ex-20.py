from random import shuffle
alunos = []
while True:
    seletor = int(input("Digite 1 para cadastrar alunos e 0 para finalizar: "))
    if seletor == 1:
        cadastrar = input("Digite o nome do aluno: ")
        alunos.append(cadastrar)
    elif seletor == 0:
        if not alunos:
            print("Lista vazia, volte e cadastre nomes!")   
            continue
        else:
            shuffle(alunos)
            print(alunos)
            break 
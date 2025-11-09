from random import choice

alunos = []

while True:
    print("Digite 1 para cadastrar alunos candidatos e 0 para sair: ")
    seletor = int(input("Digite aqui: "))
    if seletor == 1:
        limpar_a_lousa = input("Digite os nomes dos alunos candidatos a limpar a lousa: ")
        alunos.append(limpar_a_lousa)
    elif seletor == 0:
        if not alunos:
            print("Lista vazia, volte e coloque nomes nela.")
            continue
        else:
            aluno_escolhido = choice(alunos)
            print(aluno_escolhido)
            break
    else:
        print("Digite 1 para cadastrar ou 0 para finalizar e ter o resultado!")
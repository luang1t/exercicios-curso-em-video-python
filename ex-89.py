#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
alunos = []
dados = []
while True:

    nome = input('Digite seu nome: ')
    nota_um = float(input('Digite a primeira nota: '))
    nota_dois = float(input('Digite a segunda nota: '))
    media = (nota_um + nota_dois) / 2

    dados.append(nome)
    dados.append(nota_um)
    dados.append(nota_dois)
    dados.append(media)
    
    alunos.append(dados[:])
    dados.clear()
    escolha = input("Deseja continuar a cadastrar?\n[S/N]:").strip().lower()[0]
    if escolha == 's':
        continue
    elif escolha =='n':
        break
    else:
        print("Digite s ou n.")
        continue

for i,aluno in enumerate(alunos):
    print(f"{i+1} - {aluno[0]}")

aluno = int(input("Digite o numero do indice que vc deseja ver a média do aluno: "))

print(f"O aluno {alunos[aluno - 1][0]} tem a primera nota: {alunos[aluno - 1][1]} tem a segunda nota: {alunos[aluno - 1][2]} e media: {alunos[aluno - 1][3]}")
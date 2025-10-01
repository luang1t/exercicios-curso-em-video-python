aluno = dict()
aluno['nome'] = str(input("Digite seu nome: "))
aluno['media'] = float(input("Digite sua media: "))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] <= 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'    

for k,v in aluno.items():
    print(f"{k} é igual a {v}") 
 
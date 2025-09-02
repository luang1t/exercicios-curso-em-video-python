import os

def clear():
    os.system('cls')
def recebe_nota():
    notas = []
    for i in range(2):
        while True:
            try:
                nota = float(input(f"Digite a {i+1}º: "))
                if 10>= nota >= 0:
                    notas.append(nota)
                    break
                else:
                    clear()
                    print("Digite uma nota de 0 a 10")
            except ValueError:
                clear()
                print("Digite algo no contexto do programa. Tente novamente...")
    return notas            

notas = recebe_nota()
media = sum(notas)/len(notas)  
clear()
print(notas)
if media < 5:
    print(f"Reprovado com média: {media}")
elif 5 > media <= 6.9:
    print(f"Aluno foi para a recuperação com média: {media}")
else:
    print(f"Aluno foi aprovado com média: {media}")    
     



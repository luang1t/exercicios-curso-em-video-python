from time import sleep
def design_linha():
    print("-="*30)
    
def contador(inicio,fim,passo):
    if passo == 0:
        passo = 1
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    if inicio < fim:
        for _ in range(inicio,fim+1,passo):
            print(f"{_}",end=" ",flush=True)
            sleep(0.5)
        print("Fim!")
    else:
        for _ in range(inicio,fim-1,passo):
            print(f"{_}",end=" ",flush=True)
            sleep(0.5)
        print("Fim!")    
#flush = True, manda o texto direto para o terminal sem eseperar o buffer encher, assim trazendo os aspecto de contagem humana kkk.

design_linha()
contador(1,10,1)
design_linha()
contador(10,0,-2)
design_linha()

inicio = int(input("Digite o valor inicial: "))
fim = int(input("Digite o valor final: "))
passo = int(input("Digite o passo: "))
design_linha()

contador(inicio,fim,passo)
design_linha()
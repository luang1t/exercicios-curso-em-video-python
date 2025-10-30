def mostralinha():
    print('-'*30)
    
def titulo(msg):
    mostralinha()
    print(msg)
    
titulo('CURSO DE COMO FAZER CURSO')
titulo('CURSO DE COMO NÃO FAZER UM CURSO')
titulo('CURSO DE DIVA POP')

def soma(a,b=0):
    print(f"{a}+{b}={a+b}")
    return a + b

primeira_soma = soma(10,40)
print(primeira_soma)

#receber incontaveis valores
def contador(*num):
    tam = len(num)
    print(f"Recebi os valores {num} e são ao todo {tam} números.")

contador(1,2,3,4,5,6,7)

#

valores = [7,2,5,0,4]
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos]*=2
        pos+=1
#dobra(valores)
#print(valores)

def soma_dois(*numeros):
    soma = 0
    for numero in numeros:
        soma+=numero
    print(f"Somando os valores {numeros} temos {soma}")
    
soma_dois(1,2,3,4)
 

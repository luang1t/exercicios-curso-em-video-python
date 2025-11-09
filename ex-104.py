#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiInt(valor):
    while True:
        if valor.isnumeric():
            break
        else:
            valor = str(input("\033[0;31mTente novamente com um numero!\033[m\nDigite um numero:"))
    return int(valor)

input_usuario = str(input("Digite o numero: "))

validacao = leiInt(input_usuario)

print(f"\033[0;32mNúmero digitado é um inteiro:\033[m {validacao}")
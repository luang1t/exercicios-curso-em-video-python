valores = []
for i in range(2):
    valor = float(input("Digite o valor: "))
    valores.append(valor)

operacao  = input("Digite a operação 1 - Somar\n2 - Subtrair\n3 - Dividir\n4 - Multiplicar").strip()
while operacao != ('1'or'2'or'3'or'4'):
    operacao  = input("Digite a operação 1 - Somar\n2 - Subtrair\n3 - Dividir\n4 - Multiplicar")

if operacao == '1':
    soma = sum(valores)
    print(soma)
    
numero = int(input("Digite seu numero para ver seu fatorial: "))
multiplica = numero
valor_interalvel = 0
while numero > 1:
    proximo_numero = numero - 1
    valor_interalvel = multiplica * proximo_numero
    multiplica = valor_interalvel
    numero-=1
print(multiplica)    
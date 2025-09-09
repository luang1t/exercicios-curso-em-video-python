numero = int(input("Digite o valor para ter a sua fibonacci: "))

primeiro_numero = 0
segundo_numero = 1
proximo_numero = 0
while primeiro_numero <= numero:
    print(f"{primeiro_numero}")
    proximo_numero = primeiro_numero + segundo_numero
    primeiro_numero = segundo_numero
    segundo_numero = proximo_numero
    
numero = int(input("Digite um numero: "))
numero_string = str(numero)
print(f"milhar:{numero_string[0]}")
print(f"centena:{numero_string[1]}")
print(f"denzenas:{numero_string[2]}")
print(f"unidade: {numero_string[3]}")


milhar = numero // 1000 % 10
print(f"milhar:{milhar}")

centena = numero // 100 % 10
print(f"centena:{centena}")

dezena = numero // 10 % 10
print(f"dezena: {dezena}")

unidade = numero // 1 % 10
print(f"unidade: {unidade}")
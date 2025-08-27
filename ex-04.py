informacao = (input("Digite algo: "))

print(type(informacao))
print(f"composto apenas numeros: {informacao.isnumeric()}")
print(f"composto apenas letras:{informacao.isalpha()}")
print(f"composto apenas letras e/ou numeros: {informacao.isalnum()}")
print(f"composto apenas por letras maiúsculas: {informacao.isupper()}")
print(f"composto apenas por letras minúsculas: {informacao.islower()}")
print(f"composto apenas por por espaços: {informacao.isspace()}")
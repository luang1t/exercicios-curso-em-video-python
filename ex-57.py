validacao = input("Digite F para validar Feminino ou M para validar Masculino (0):").lower().strip()[0]
while validacao not in "MmFf":
   validacao = input("Digite F para validar Feminino ou M para validar Masculino (1):").lower().strip()[0]
print(f"Validação realizada '{validacao}'")   
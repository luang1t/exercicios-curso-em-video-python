numeros = (
    "zero", "um", "dois", "três", "quatro", 
    "cinco", "seis", "sete", "oito", "nove", 
    "dez", "onze", "doze", "treze", "quatorze", 
    "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
)

user_input = int(input("Um numero de 0 a 20: "))
while True:
    if user_input <= 20 and user_input >= 0:
        print(numeros[user_input])
        break
    else:
        user_input = int(input("Um numero de 0 a 20: "))
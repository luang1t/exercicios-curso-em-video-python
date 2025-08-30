import os
def clear():
    return os.system("cls")
def recebe_numeros():
    numeros = []
    for i in range(2):
        while True:
            try:
                numero = float(input(f"Digite o {i+1}º numero: "))
                numeros.append(numero)
                break   
            except ValueError:
                clear()
                print("Digite apenas números.")
    return numeros         

numeros = recebe_numeros()

if numeros[0] > numeros[1]:
    print(f"O maior numero é o primeiro {numeros[0]}")
elif numeros[1] > numeros[0]:
    print(f"O maior numeros é o segundo {numeros[1]}") 
else:
    print(f"Ambos tem os mesmos numeros")       
    
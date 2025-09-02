import os
def clear():
    os.system('cls')
def recolhe_dados():
    dados_imc = {"peso": [] , "altura" : []}
    while True:
        try:
            peso = float(input("Digite o seu peso: "))
            altura = float(input("Digite sua altura: "))
            dados_imc["altura"].append(altura)
            dados_imc["peso"].append(peso)
            return dados_imc
        except ValueError:
            clear()
            print("Digite algo no contexto do programa.")

dados = recolhe_dados()

print(dados)
for i in range(len(dados['peso'])):
    peso = dados["peso"][i]
    altura = dados["altura"][i]
    imc = peso/(altura**2)

print(f"{imc:.2f}")
if imc < 18.5:
    print("Abaixo do peso!")
elif 18.5<imc<=25:
    print("Peso ideal")
elif 25<imc<=30:
    print("Sobrepeso")
elif 30<imc<=40:
    print("Obesidade")
else:
    print("Obesidade mórbida")        

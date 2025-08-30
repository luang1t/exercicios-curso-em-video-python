import os

def clear():
    return os.system('cls')
def receber_ano():
    while True:
        try:
            ano_nascimento = int(input("Digite seu ano de nascimento: "))
            return ano_nascimento
        except ValueError:
            clear()
            print("Digite o ano de nascimento nesse modelo ex: '1997'.")

verificar_ano = receber_ano()
ano_atual = 2025

if (ano_atual - verificar_ano > 18):
    clear()
    tempo_excedente = (ano_atual - verificar_ano) - 18
    print(f"Passou do tempo, está à {tempo_excedente} anos em divida com a nação, vá até um quartel para se regularizar!")
elif(ano_atual - verificar_ano < 18):
    tempo_faltante = 18 - (ano_atual - verificar_ano)
    clear()
    print(f"Ainda é cedo, volte daqui {tempo_faltante} anos quando completar 18!")
else:
    clear()
    print("Está apto ao alistamento!")    
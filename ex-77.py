palavras = ('peido','escada','sehloco','peidin','roleshito','shibata')

for palavra in palavras:
    for letra in palavra:
        if letra in "aeiou":
            print(f'{palavra} - {letra}')

while True:
    frase = str(input("Digite uma frase pra ver se é palindromo: ")).strip().upper()
    dividindo_string = frase.split()
    frase_junta = ""
    inverso =""
    for i in range(len(dividindo_string)):
        frase_junta += dividindo_string[i]
    print(frase_junta)    
    inverso =""
    for i in range(len(frase_junta)-1,-1,-1):
        inverso+=frase_junta[i]
    if inverso == frase_junta:
        print("Palindromo")
        break 
    else: 
        print("Não é palindromo")       
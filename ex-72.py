tupla = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez')


numero = int(input("Digite um numero de 0 a 10: "))
while True:
    if 0 <= numero <=10:
        if numero in range(len(tupla)):
            print(tupla[numero])
            break           
    else:
        numero = int(input("Tente novamente!\nDigite um numero de 0 a 10: "))        
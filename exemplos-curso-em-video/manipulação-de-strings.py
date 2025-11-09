frase = 'Curso em vídeo python'
#APENAS O QUARTO CARACTERE
print(frase[3])

#INICIA NO TERCEIRO, MOSTRANDO ELE, E TERMINA NO TERCEIRO CARACTERE SEM MOSTRAR ELE, NO CASO O 13.
print(frase[3:13])

#PEGA TUDO QUE VENHA ANTES DE 13 E NÃO MOSTRA O 13
print(frase[:13])

#PEGA TUDO QUE VENHA DEPOIS DE 13 CONTANTO O 13 TBM
print(frase[13:])

#PEGA UM INICIO E UM FIM SEM MOSTRAR O CARACTERE DO FIM PULANDO DE 2 EM 2.
print(frase[5:21:2])
print(frase[::2])

#
#print('Oi')
#print("""Python é uma linguagem poderosa, versátil e divertida! Com ela, é possível automatizar tarefas, analisar dados, criar jogos e até desenvolver inteligência artificial.
#Lembre-se: praticar todos os dias é o caminho para a maestria. 🚀""")

#CONTAR QUANTAS VEZES TAL COISA APARECEU NA STRING
print(frase.count('O'))

#USANDO FUNÇÕES PARA TRANSFORMAR A STRING
print(frase.upper().count('O'))

#FUNÇÃO PARA TAMANHO DA STRING
print(len(frase))

#FUNÇÃO PARA REMOVER OS ESPAÇOS DA STRING TBM REDUZEM O SEU TAMANHO APÓS O STRIP
nova_frase = " Todos devem saber lógica de programação  "


#ANTES 
print(len(nova_frase))


#DEPOIS
print(len(nova_frase.strip()))

#PARA ALTERAR UMA STRING PRIMEIRO VC PRECISA UTILIZAR UM REPLACE PARA ALTERAR E DEPOIS ATRIBUIR ESSA ALTERAÇÃO A VARIAVEL INICIAL
frase_alterada = "Todos querem doce"
print(frase_alterada)
frase_alterada = frase_alterada.replace("doce","bala")
print(frase_alterada)


#IDENTIFICAR SE TEM UMA UM ELEMENTO NA STRING
print('doce' in frase_alterada)

#SABER A POSIÇÃO INICIAL DE UM ELEMENTO
print(frase_alterada.find('querem'))

#SÓ É POSSIVEL ACHAR SE ESTIVER NA MESMA CAIXA, OU SEJA SE ESTIVER ESCRITO assim E VOCE PESQUISAR AsSiM NÃO VAI ACHAR E VAI DAR -1 
print(frase_alterada.find('QUEREM'))

#MAS EXISTE UM METODO PARA PODERMOS DEIXAR HOMOGENEO E ACHAR ONDE ESTÁ O PRIMEIRO QUE É USANDO UPPER OU LOWER QUE ALTERÃO TODA A STRING PARA CAIXA ALTA OU BAIXA
print(frase_alterada.upper().find("QUEREM"))

#DIVIDIR STRING EM PYTHON É TRANSFORMLA EM UMA LISTA. É POSSIVEL FAZER ESSA DIVISÃO USANDO O SPLIT, DIVISAO É FEITA NOS ESPAÇOS.
print(frase_alterada.split())
lista_frase = frase_alterada.split()
print(lista_frase[0])

#FAZENDO UMA IDENTIFICAÇÃO DENTRO DO SPLIT DA STRING, QUERO SABER A QUINTA LETRA DA PRIMEIRA PALAVRA
print(lista_frase[0][4])
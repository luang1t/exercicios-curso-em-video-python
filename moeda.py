def aumentar(preco,taxa):
    valor = preco+(preco*(taxa/100))
    return valor

def diminuir(preco,taxa):
    valor = preco-(preco*(taxa/100))
    return valor

def dobro(preco):
    valor = preco*2
    return valor

def metade(preco):
    valor = preco/2
    return valor

def conversor(preco,moeda="R$: "):
    valor = preco
    return f"{moeda}{valor:8.2f}".replace('.',',')
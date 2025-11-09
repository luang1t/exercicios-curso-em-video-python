produtos = (
    'Arroz',2.5,
'Feijao',4.5,
'Tapioca',8.99

)

for i in range(0,len(produtos),2):
    print(f"{produtos[i]:.<30}R$:{produtos[i+1]}")

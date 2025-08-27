from math import trunc
distancia = float(input("Digite a distancia percorrida em Km: "))

if distancia <= 200:
    print(f"Viagem curta de {trunc(distancia)}Km")
    print(f"Preço da viagem R$:{distancia*0.5:.2f}")
else:
    print(f"Viagem longa de {trunc(distancia)}Km")
    print(f"Preço da viagem R$:{distancia*0.45:.2f}")    
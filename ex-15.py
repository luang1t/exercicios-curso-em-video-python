km_percorridos = float(input("Digite quantos Km você percorreu durante o aluguel: "))
dias_alugados = int(input("Digite durante quantos dias você alugou o carro: "))

print(f"Você utilizou o carro por {dias_alugados} dias e percorreu {km_percorridos}Km.")
print(f"Nossa forma de cobrar o aluguel é:\nR$:60.00 por dia\nR$0.15 por Km rodado.")
print(f"Dias alugados = R$:{dias_alugados*60:.2f}\nKm percorridos = R$:{km_percorridos*0.15:.2f}")
print(f"Total a pagar: R$:{(dias_alugados*60)+(km_percorridos*0.15):.2f}")
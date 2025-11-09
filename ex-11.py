largura = float(input("Digite a largura da sala: "))
altura = float(input("Digite a altura da sala: "))

lata_de_tinta = 2

print(f"Seu apartamento tem {largura*altura:.2f}m² uma lata de tinta pinta {lata_de_tinta}m² então vai precisar de {(largura*altura)/lata_de_tinta:.0f} latas")
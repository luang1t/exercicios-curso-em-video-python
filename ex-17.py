from math import hypot,trunc

cateto_oposto = float(input("Digite o cateto oposto: "))
cateto_adjacente = float(input("Digite o cateto adjacente: "))

hipotenusa = hypot(cateto_oposto,cateto_adjacente)

print(trunc(hipotenusa))

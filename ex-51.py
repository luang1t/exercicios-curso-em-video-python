termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = (razao*10)+termo

for i in range(termo,decimo,razao):
    print({i},end=" -> ")
print("Fim")    
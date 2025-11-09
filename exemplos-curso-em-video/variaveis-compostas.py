lanche = ('hamburg','suco','pizza','pudim','canudo','bocha')
#lanche[1]='Refrigerante'
#tuplas são imutaveis.
print(sorted(lanche))
print(lanche[:2])
for comid in lanche:
    print(f'Eu vou comer um belo de um {comid}')

for comid in range(len(lanche)):
    print

for comida in lanche:
    print(f"Vou comer muito {comida} meu!") 

for i in range(0,len(lanche)):
    print(f"{i+1}º vou comer {lanche[i]}")

for pos, comida in enumerate(lanche):
    print(f"{pos+1}º vou comer {comida}")


a = (2,5,4)
b = (5,8,1,2)
c = a + b
d = b + a
print(d,len(d),d.count(2))
print(c,len(c),c.count(5))
print(d.index(8))
pessoa = ('Luan', 24, 'M', 68.50)
#del(pessoa)
print(pessoa)
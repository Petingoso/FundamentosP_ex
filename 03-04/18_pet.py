# Isto é um crime de guerra
# Deve haver melhor maneira mas não sei
# Sorry

amount = eval(input("Diga uma quantia (€): "))
amount = amount*100 # centimos

notas_50    = 0
notas_10    = 0
notas_5     = 0
moedas_200  = 0
moedas_100  = 0
moedas_50   = 0
moedas_20   = 0
moedas_10   = 0
moedas_5    = 0
moedas_2    = 0
moedas_1    = 0

while amount > 0:
    if(amount>=5000):
        notas_50+=1
        amount-=5000
        continue
    if(amount>=1000):
        notas_10+=1
        amount-=1000
        continue
    if(amount>=500):
        notas_5+=1
        amount-=500
        continue
    if(amount>=200):
        moedas_200+=1
        amount-=200
        continue
    if(amount>=100):
        moedas_100+=1
        amount-=100
        continue
    if(amount>=50):
        moedas_50+=1
        amount-=50
        continue
    if(amount>=20):
        moedas_20+=1
        amount-=20
        continue
    if(amount>=10):
        moedas_10+=1
        amount-=10
        continue
    if(amount>=5):
        moedas_5+=1
        amount-=5
        continue
    if(amount>=2):
        moedas_2+=1
        amount-=2
        continue
    if(amount>=1):
        moedas_1+=1
        amount-=1
        continue
    amount = -1

print(f"Notas de 50:    {notas_50}")
print(f"Notas de 10:    {notas_10}")
print(f"Notas de 5:     {notas_5}")
print(f"Moedas de 2:    {moedas_200}")
print(f"Moedas de 1:    {moedas_100}")
print(f"Moedas de 0.50: {moedas_50}")
print(f"Moedas de 0.20: {moedas_20}")
print(f"Moedas de 0.10: {moedas_10}")
print(f"Moedas de 0.05: {moedas_5}")
print(f"Moedas de 0.02: {moedas_2}")
print(f"Moedas de 0.01: {moedas_1}")


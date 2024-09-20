x = eval(input("Introduza a quantia:"))
# x = XXX.XX
x *= 100
# Multiplicar por 100 para obter só números inteiros
# x = XXXXX
nota50=nota20=nota10=nota5=moeda2=moeda1=cent50=cent20=cent10=cent5=cent2=cent1 = 0
if x//5000!=0:
    #há alguma nota de 50€
    nota50 = x//5000
    x%=5000
if x//2000!=0:
    #há alguma nota de 20€
    nota20 = x//2000
    x%=2000
if x//1000!=0:
    #há alguma nota de 10€
    nota10 = x//1000
    x%=1000
if x//500!=0:
    #há alguma nota de 5€
    nota5 = x//500
    x%=500
if x//200!=0:
    #há alguma moeda de 2€
    moeda2 = x//200
    x%=200
if x//100!=0:
    #há alguma moeda de 1€
    moeda1 = x//100
    x%=100
if x//50!=0:
    #há alguma moeda de 0.50€
    cent50 = x//50
    x%=50
if x//20!=0:
    #há alguma moeda de 0.20€
    cent20 = x//20
    x%=20
if x//10!=0:
    #há alguma moeda de 0.10€
    cent10 = x//10
    x%=10
if x//5!=0:
    #há alguma moeda de 0.05€
    cent5 = x//5
    x%=5
if x//2!=0:
    #há alguma moeda de 0.20€
    cent2 = x//2
    x%=2
if x//1!=0:
    #há alguma moeda de 0.01€
    cent1 = x//1
    x%=1
print("Notas de    50€:", int(nota50))
print("Notas de    20€:", int(nota20))
print("Notas de    10€:", int(nota10))
print("Notas de     5€:", int(nota5))
print("Moedas de    2€:", int(moeda2))
print("Moedas de    1€:", int(moeda1))
print("Moedas de 0,50€:", int(cent5))
print("Moedas de 0,20€:", int(cent20))
print("Moedas de 0,10€:", int(cent10))
print("Moedas de 0,05€:", int(cent5))
print("Moedas de 0,02€:", int(cent2))
print("Moedas de 0,01€:", int(cent1))

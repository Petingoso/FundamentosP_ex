x = eval(input("Escreva um inteiro positivo\n? "))
o=0

while x!=0:
    d = x%10
    x//=10
    o = o*10 + d
print("O número invertido é", o)
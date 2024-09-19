x = eval(input("Escreva um número\n-> "))

i=0
x2 = 1+x
while x!=0:
    #ler o número de trás para a frente
    #mesmo procedimento do ex. 10
    d=x%10
    x//=10
    x2 = x2*10 + d
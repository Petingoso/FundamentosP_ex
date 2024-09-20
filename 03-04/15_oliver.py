x = eval(input("Escreva um número \n?"))
cap = x
bck = 0
while x != 0:
    cap *= 10
    bck = bck*10 + (x%10)
    x //= 10
print(cap + bck)

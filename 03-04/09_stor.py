ok = True
num = 0

while ok:
    dig = eval(input("Escreva um dígito (-1 para terminar): "))
    if dig ==-1:
        ok = False
    else:
        num = dig + 10*num
print("O número é ", num)


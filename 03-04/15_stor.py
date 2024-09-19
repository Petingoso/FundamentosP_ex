# input = 347
# capicua = 347
# inverter 347 (num) e colar no capicua (347 743)
num = eval(input("Escreva um número: "))

i = 0
capicua = num 
while num:
    capicua = capicua*10 + num%10
    num //=10


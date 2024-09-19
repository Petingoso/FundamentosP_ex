num1 = eval(input("Escreva o 1º número: "))
num2 = eval(input("Escreva o 2º número: "))
num3 = eval(input("Escreva o 3º número: "))

if num1 > num2 and num1>num3:
    #num1 é o maior
    maior = "1º"
elif num2 > num1 and num2 > num3:
    #num2 é o maior
    maior = "2º"
elif num3 > num1 and num3 > num2:
    #num3 é o maior
    maior = "3º"

print("O número maior é o ", maior)
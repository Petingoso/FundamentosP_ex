from math import sqrt as sqrt

num1 = eval(input("Escreva o 1º número real: "))
num2 = eval(input("Escreva o 2º número real: "))
num3 = eval(input("Escreva o 3º número real: "))
num4 = eval(input("Escreva o 4º número real: "))
num5 = eval(input("Escreva o 5º número real: "))

media = (num1+num2+num3+num4+num5)/5
desv1 = (num1-media)**2
desv2 = (num2-media)**2
desv3 = (num3-media)**2
desv4 = (num4-media)**2
desv5 = (num5-media)**2
medDesv = (desv1+desv2+desv3+desv4+desv5)/5
desvPadr = sqrt(medDesv)

print("A média é: ", media, "\nO desvio-padrão é: ", desvPadr)
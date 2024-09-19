num = eval(input("Escreva um inteiro: "))

num_impar = 0

i=1
j=1

while num > 0:
    dig = num % 10*i

    if (dig % 2 != 0):
        num_impar = num_impar + dig*1*j
        j*=10

    num //= 10
print("Resultado é :", num_impar)


num = eval(input("Escreva um inteiro positivo: "))

soma = 0

while num:
    soma = soma + (num%10)
    num //=10

print("Resultado é :", soma)


num = eval(input("Escreva um inteiro positivo: "))

num_invertido = 0

while num:
    # primeiro digito do invertido é o último do num 
    # 123 -> 3 passa a ser o primeiro de invertido
    num_invertido= num_invertido*10 + (num%10)
    num //=10

print("Resultado é :", num_invertido)


n = 1
while True:
    n = eval(input("Escreva um número de segundos\n(um número negativo para terminar)\n? "))
    if n>=0:
        day = n/86400
        print("O número de dias correspondente é: ", day)
        print(" ")
    else:
        break
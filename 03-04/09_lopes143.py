expr=0
while True:
    n = eval(input("Escreva um dígito\n(-1 para terminar)\n? "))
    if n<0:
        break
    expr = expr*10 + n
print("O número é: ", expr)
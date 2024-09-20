expr = ""

while True:
    n = eval(input("Escreva um dígito\n(-1 para terminar)\n? "))
    if n<0:
        break
    expr = expr+str(n)
print("O número é:", expr)
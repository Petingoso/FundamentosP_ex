x = ""

while True:
    num = eval(input("Escreva um dígito: "))
    if (num == -1):
        break
    x = x + str(num)

print("Número é:",x)

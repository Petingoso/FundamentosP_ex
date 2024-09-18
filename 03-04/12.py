x = eval(input("Qual o valor de x:"))
n = eval(input("Qual o valor de n:"))

def factorial(num):
    if (num==0):
        return 1

    result = 1
    for i in range(1,num+1):
        result = result * i
    return result

def obter_termo(i):
    if (i == 0):
        return 1

    termo_anterior = (x**(i-1))/(factorial(i-1))
    termo_atual = termo_anterior * (x/i)
    return  termo_atual

soma = 0
for i in range(n+1):
    soma = soma + obter_termo(i)

print(soma)

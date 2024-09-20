x = eval(input("Qual o valor de x\n? "))
n = eval(input("Qual o valor de n\n? "))

def factorial(num):
    f = 1
    while num>0:
        f=f*num
        num-=1
    return(f)
    
def exponential(base, expoent):
    return(base**expoent)

#OLD CODE
#s = 1
#for i in range(n+1):
#    s += exponential(x, n)/factorial(n)

def termo(i):
    numAnter = (exponential(x, i-1))/(factorial(i-1))
    numAtual = numAnter * (x/i)
    return numAtual

soma = 1
for i in range(1, n+1):
    soma += termo(i)
print("O valor da soma é ", soma)

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

    
print(factorial(n))

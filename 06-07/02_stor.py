from math import ceil,log10
def explode(n):
    if (isinstance(n,int) and n>0):
        r = ()
        while n:
            r = (n % 10,) + r
            n //= 10
        return r

    raise ValueError("argumento não inteiro positivo")
print(explode(34500))

## versão for
def explode2(n):
    if (isinstance(n,int) and n>0):
        r = ()
        for i in range(ceil(log10(n+1))):
            r = (n%10,) +r 
            n //= 10
        return r

    raise ValueError("argumento não inteiro positivo")
print(explode2(34500))

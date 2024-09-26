def explode(n):
    if (isinstance(n,int) and n>0):
        r = ()
        while n:
            r = (n % 10,) + r
            n //= 10
        return r

    raise ValueError("argumento não inteiro positivo")
print(explode(34500))

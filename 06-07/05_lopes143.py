def explode(n):
    t = ()
    if not isinstance(n, int):
        raise TypeError("Tipo de valor inválido")
    elif n<=0:
        raise ValueError("Valor inválido")
    while n!=0:
        d = n % 10
        n//=10
        t = (d, ) + t
    return t

def implode(t):
    r=0
    if not isinstance(t, tuple):
        raise TypeError("Não é um tuplo")
    for i in t:
        if not isinstance(i, int):
            raise ValueError("Valor no tuplo inválido)")
        r = r*10+i
    return r

def filtra_pares(t):
    if not isinstance(t, tuple):
        raise TypeError("Não é um tuplo")
    r = ()
    for i in t:
        if not isinstance(i,int):
            raise ValueError("Valor do tuplo inválido")
        if i%2==0:
            r = r + (i, )
    return r
        
def algarismos_pares(x):
    return implode(filtra_pares(explode(x)))

print(algarismos_pares(6643399766641))
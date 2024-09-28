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

print(explode(34500))
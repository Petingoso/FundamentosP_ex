def implode(t):
    r=0
    if not isinstance(t, tuple):
        raise TypeError("Não é um tuplo")
    for i in t:
        if not isinstance(i, int):
            raise ValueError("Valor no tuplo inválido)")
        r = r*10+i
    return r

print(implode((3, 4, 0, 0, 4)))
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

print(filtra_pares((2, 5, 6, 7, 9, 1, 8, 8)))
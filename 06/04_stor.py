def filtra_pares(t):
    if isinstance(t,tuple):
        r = ()
        for d in t: 
            if not isinstance(d,int) or not(0<=d<=9):
                raise ValueError("elemento não algarismo")
            if d%2==0:
                r += (d,)
        return r
    raise ValueError("argumento não tuplo")
print(filtra_pares((2,5,6,7,9,1,8,8)))

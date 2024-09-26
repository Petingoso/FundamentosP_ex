def serie_geom(r,n):
    i=0
    soma=0
    if (isinstance(r,int) and r >=0) and (isinstance(n,int) and n >=0):
        while i<n+1:
            soma = soma + r**i
            i=i+1
        return soma
    else:
        raise ValueError("Argumento incorreto")
print(serie_geom(2,4))
print(serie_geom(100,0))
print(serie_geom(100,-1))

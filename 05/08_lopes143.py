def serie_geom(r, n):
    if not (isinstance(r, int) and isinstance(n, int)):
        raise TypeError("Input não inteiro")
    elif n<0:
        raise ValueError("serie_geom: argumento incorrecto")
    geom=0
    for i in range(0, n+1):
        geom += r**i
    return geom

print(serie_geom(2, 4))
print(serie_geom(100, 0))
print(serie_geom(100, -1))
def valor(q, j, n):
    if q<0 or j<0 or j>1 or n<0:
        raise ValueError()
    return q*((1+j)**n)
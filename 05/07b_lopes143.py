def valor(q, j, n):
    if q<0 or j<0 or j>1 or n<0:
        raise ValueError()
    return q*((1+j)**n)

def duplicar(q, j):
    c=0
    while valor(q, j, c) < 2*q:
        c+=1
    return c
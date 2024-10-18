from functools import reduce

def lista_digitos(n):
    return list(map(lambda x:int(x), str(n)))

def produto_digitos(n, fn):
    return reduce(lambda x,y:x+y, filter(n), lista_digitos(n, fn))


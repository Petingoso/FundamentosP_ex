from functools import reduce

def filtra(lst, tst):
    return list(filter(tst, lst))

def transforma(lst, fn):
    return list(map(fn, lst))

def acumula(lst, fn):
    return reduce(fn,lst)


print(filtra([1, 2, 3, 4, 5], lambda x : x % 2 == 0))
print(transforma([1, 2, 3, 4], lambda x : x ** 3))
print(acumula([1, 2, 3, 4], lambda x, y : x + y))
def apaga1(t, k):
    v = False
    t2 = ()
    for i in t:
        if k==i and v==False:
            v = True
        else:
            t2 = t2 + (i, )
    return t2

print(apaga1((1, 2, 4, 2, 1), 2))
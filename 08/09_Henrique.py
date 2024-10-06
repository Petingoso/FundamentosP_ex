def num_occ_lista(l,x):
    c = 0
    while l:
        if type(l[0]) == list:
            l += l[0]
        else:
            c += (l[0] == x)
        l = l[1:]
    return c

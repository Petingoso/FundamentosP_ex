def num_occ_lista(w,n):
    c=0
    i=0
    while i < len(w):
        if (isinstance(w[i],list)):
            w+=w[i]
            w.remove(w[i])
            i=i-1
        else:
            if w[i]==n:
                c+=1
        i+=1
    return c

print(num_occ_lista([1, 2, 3, 4, 3], 3))
print(num_occ_lista([1, [[[1]], 2], [[[2]]], 2], 2))


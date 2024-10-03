def soma_cumulativa(w):
    i = 0
    r = list(w)
    while i < len(w):
        for j in range(0,i):
            r[i]+=w[j]
        i+=1
    return r

print(soma_cumulativa([1, 2, 3, 4, 5]))


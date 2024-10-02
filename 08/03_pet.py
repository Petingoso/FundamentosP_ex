def soma_cumulativa(w):
    i = 0
    while i < len(w):
        for j in range(0,i):
            w[i]+=w[j]
    i+=1
    return w

soma_cumulativa([1, 2, 3, 4, 5])


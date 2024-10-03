def soma_cumulativa(w):
    for i in range(1,len(w)):
        w[i] += w[i-1]
    return w 
print(soma_cumulativa([1,2,3,4,5]))

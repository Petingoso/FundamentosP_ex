def posicoes_maximo(w):
    if len(w)<0:
        return ()
    
    max=w[0]
    r = ()
    for i in range(len(w)):
        if w[i] == max: 
            r += (i,)
        elif w[i] > max: 
            max = w[i]
            r = (i,)
    return r
print(posicoes_maximo((1,2,3,2,1,2,3)))

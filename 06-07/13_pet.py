def apaga1(tup,k):
    i = 0
    for i in range(len(tup)):
        if tup[i] ==k:
            break
    return tup[0:i] + tup[i+1:]

def permutacao(w1,w2):
    i=0
    z1 = w1
    z2 = w2
    while i<len(w1) and i <len(w2): # percorrer lista e ir tirando elementos
        z1=apaga1(z1,w1[i])
        z2=apaga1(z2,w2[i])
        i+=1
    if (z1 == z2) and (z1 == ()): # ambas vazias
        return True 
    
    return False

print(permutacao((1, 2, 3), (1, 2, 3)))
print(permutacao((1, 2, 3), (2, 3, 1)))
print(permutacao((1, 1, 1, 2, 3), (1, 2, 3)))
print(permutacao((1, 2, 3), (1, 2, 3, 4)))




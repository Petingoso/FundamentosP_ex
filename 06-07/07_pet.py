def amigas(t):
    amount = 0
    for i in range(len(t[0])):
        print(t[0][i], t[1][i])
        if t[0][i] != t[1][i]:
             amount+=1


    if amount: # pelo menos 1 diferença
        return (( amount/len(t[0]) )* 100) < 10 # tamanho / numero vezes(>0), * 100 para percentagem
    else:
        # print(len(t[0]))
        return True # caso 0 difs

print(amigas(('amigas','amigas')))
print(amigas(('amigas','asigos')))
print(amigas(('amigassssss','amigosssssss')))

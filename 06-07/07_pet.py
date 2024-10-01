def amigas(t1,t2):
    if len(t1) != len(t2):
        return False 

    amount = 0
    for i in range(len(t1)):
        if t1[i] != t2[i]:
             amount+=1

    if amount: # pelo menos 1 diferença
        # tamanho / numero vezes(>0), * 100 para percentagem
        return (( amount/len(t1) )* 100) < 10     
    else:
        return True # caso 0 difs

print(amigas('amigas','amigas'))
print(amigas('amigas','asigos'))
print(amigas('amigassssss','amigosssssss'))

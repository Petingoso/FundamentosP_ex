def reconhece(c):
    l = False
    n = False
    for i in c:
        if i in ['A','B','C','D'] and n==False:
            l = True
        elif i in ['1','2','3','4'] and l==True:
            n = True
        else:
            return False
    return l and n

print(reconhece('A1'))
print(reconhece('ABBBBCDDDD23311'))
print(reconhece('ABC12C'))
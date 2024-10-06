def reconhece(p, s):
    pPos = 0
    check = 0
    for sPos in range(len(s)):   
        if p[0] == s[sPos] and check!=True:
            #encontrou o 1º num de p na lista s
            #e ainda não rodou o check
            for pPos in range(len(p)):
                if (sPos+pPos)>(len(s)-1):
                    #a verificação sai fora da lista s
                    check = False
                    break
                elif p[pPos] == s[sPos+pPos]:
                    check = True
                else:
                    check = False
                    break    
    
    return check

print(reconhece([1,2,3], [2,1,2,3,4,5]))
print(reconhece([4,3,4], [2,1,4,2,3,4,5]))
print(reconhece([5,2,7], [5,2,7]))
print(reconhece([9,4], [3,2,4,2,9,4]))
print(reconhece([7,4,3], [7,4,7,4,3,7,2,7]))
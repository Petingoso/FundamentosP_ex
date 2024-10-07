def conta_palavras(string):
    outDic = {}
    for i in string.split(' '):
        if i in outDic:
            outDic[i]+=1
        else:
            outDic[i]=1
    return outDic

cc = 'a aranha arranha a ra a ra arranha a aranha nem a aranha arranha a ra nem a ra arranha a aranha'

print(conta_palavras(cc))
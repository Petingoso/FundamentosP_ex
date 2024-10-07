def metabolismo(dici):
    outDic={}
    for i in dici:
        if dici[i][0]=='M':
            outDic[i]=66+(6.3*dici[i][3])+(12.9*dici[i][2])+(6.8*dici[i][1])
        elif dici[i][0]=='F':
            outDic[i]=655+(4.3*dici[i][3])+(4.7*dici[i][2])+(4.7*dici[i][1])
    return outDic

d = {'Maria' : ('F', 34, 1.65, 64), 'Pedro': ('M', 34, 1.65, 64), 'Ana': ('F', 54, 1.65, 120), 'Hugo': ('M', 12, 1.82, 75)}

print(metabolismo(d))
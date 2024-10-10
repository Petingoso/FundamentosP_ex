def conta_palavras(str):
    dic = {}
    word = ""
    for c in str:
        if c != " ":
            word+=c 
        else:
            if word in dic:
                dic[word]+=1
            else:
                dic[word]=1
            word = ""
    return dic

cc = "a aranha arranha a ra a ra arrnha a aranha nem a aranha arranha a ra nem a ra arranha a aranha"
print(conta_palavras(cc))

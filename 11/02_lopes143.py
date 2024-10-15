def conta_vogais(nome):
    dict={'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    f=open(nome, 'r')
    for i in f.readlines():
        for i2 in i:
            if i2 in dict:
                dict[i2]+=1
    f.close()
    return dict

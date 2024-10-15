def conta_linhas(nome):
    c=0
    f=open(nome, 'r')
    for i in f.readlines():
        if len(i)>0:
            c+=1
    f.close()

    return c
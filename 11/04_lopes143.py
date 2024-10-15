def concatena(lst, nome):
    f=open(nome, 'w')
    for i in lst:
        tmp = open(i, 'r')
        f.write(tmp.read())
        tmp.close()
    f.close()
    return
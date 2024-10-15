def inverte(nome1, nome2):
    f1=open(nome1, 'r')
    f2=open(nome2, 'w')
    linhas=f1.readlines()

    for i in linhas[::-1]:
        f2.write(i)
    
    f1.close()
    f2.close()
    return
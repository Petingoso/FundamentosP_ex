def amigas(c1, c2):
    h = 0
    if len(c1)!=len(c2):
        raise ValueError()
    for i in range(len(c1)):
        if c1[i]==c2[i]:
            h+=1
    r = h/len(c1)
    return r>=0.9

print(amigas('amigas', 'amigas'))
print(amigas('amigas', 'asigos'))
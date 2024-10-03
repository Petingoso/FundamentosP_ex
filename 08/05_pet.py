def escreve_matrix(m):
    r = ''
    for l in m:
        for x in l:
            r += str(x) + '\t'
        r= r[:-1]+'\n'
    return(r[:-1])
m = [[1, 2, 3], [4, 5, 6]]
print(escreve_matrix(m))


# checking chato
def elemento_matriz(m,i,j):
    if isinstance(m,list):
        if isinstance(i,int) and 0<=i<=len(m):
            for l in m:
                if len(l) != len([0]):
                    raise ValueError('argumento não matrix')
                for x in l:
                    if not isinstance(x,(int,float)):
                        raise ValueError('argumento não matriz')
            if isinstance(j,int) and 0<=j<len(m[0]):
                return m[i][j]
            raise ValueError('indice invalido coluna')
        raise ValueError('indice invalido linha')
    raise ValueError('argumento não matriz')


# num linhas    -> num colunas 
# num colunas   -> num linhas 
# 1o elemento de cada linha -> 1o elemento cada coluna

def escreve_matrix(m):
    print('\n'.join(['\t'.join([str(x) for x in l]) for l in m]))

def transposta(m):
    r=[[] for linha in range(len(m[0]))]
    for linha in range(len(m[0])):
        for col in range(len(m)):
            r[linha].append(m[col][linha])

    return r



escreve_matrix([[1, 2, 3], [4, 5, 6]])
escreve_matrix(transposta([[1, 2, 3], [4, 5, 6]]))

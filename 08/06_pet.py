def escreve_matriz(m):
    print('\n'.join(['\t'.join([str(x) for x in l]) for l in m]))

def soma_mat(m1,m2):
    for l in range(len(m1)):
        for c in range(len(m1[0])):
            m1[l][c] = m1[l][c]+m2[l][c]
    return m1
m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

m2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(escreve_matriz(soma_mat(m1, m2)))


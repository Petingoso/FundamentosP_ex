def escreve_matrix(m):
    print('\n'.join(['\t'.join([str(x) for x in l]) for l in m]))

def prod_int (A,lin,B,col):
    r = 0 
    for i in range(len(B)): # num colunas B 
        r += A[lin][i]*B[i][col]
    return r

def multiplica_mat(A,B):
    R = [[0 for j in range(len(B[0]))] for i in range(len(A))] # inicializar lista vazia com tamanho certo
    for i in range(len(A)):
        for j in range(len(B[0])):
            R[i][j]= prod_int(A,i,B,j)
    return R

m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
escreve_matrix(multiplica_mat(m1,[[1,0,0],[0,-1,0],[0,0,1]]))

def multiplica_mat1(A,B):
    R = [[0 for j in range(len(B[0]))] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                R[i][j]+= A[i][k]*B[k][j]
    return R

escreve_matrix(multiplica_mat1(m1,[[1,0,0],[0,-1,0],[0,0,1]]))

# m1 =  [0, 1, 4]  m2 = [0, 3]
#       [2, 3, 7]       [1, 4]
#                       [2, 5]
#
# [0*0 + 1*1 + 4*2    0*3 + 1*4 + 4*2]
# [2*0 + 3*1 + 7*2    2*3 + 3*4 + 7*5]
# 
# [m1[0][0]*m2[0][0] + m1[0][1]*m2[1][0] + m1[0][2]*m2[2][0]     m1[0][0]*m2[0][1] + m1[0][1]*m2[1][1] + m1[0][2]*m2[2][1] ]
# [m1[1][0]*m2[0][0] + m1[1][1]*m2[1][0] + m1[1][2]*m2[2][0]     m1[1][0]*m2[0][1] + m1[1][1]*m2[1][1] + m1[1][2]*m2[2][1] ]

def multiplica_mat(matriz_um, matriz_dois):
    outMatriz = [[0 for i in range(len(matriz_dois[0]))] for i in range(len(matriz_um))] # criar a lista de output do tamanho certo
    for m in range(len(matriz_um)): # linhas da m1
        for r in range(len(matriz_dois[0])): # colunas da m2
            for n in range(len(matriz_dois)): #linhas da m2
                outMatriz[m][r] += matriz_um[m][n]*matriz_dois[n][r]

    return outMatriz

def escreve_matriz(matrix):
    outputMatrix=''
    for row in matrix:
        for column in row:
            outputMatrix = outputMatrix + str(column) + '\t'
        outputMatrix += '\n'
    
    return outputMatrix
print(escreve_matriz(multiplica_mat([[0, 1, 4] ,[2, 3, 7]], [[0, 3], [1, 4], [2, 5]])))
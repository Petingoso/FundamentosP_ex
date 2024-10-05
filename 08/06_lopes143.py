def soma_mat(matriz_um, matriz_dois):
    outMatriz = matriz_um
    if len(matriz_um) != len(matriz_dois):
        raise ValueError()
    for i in range(len(matriz_um)):
        if len(matriz_um[i])!= len(matriz_dois[i]):
            raise ValueError()
        for j in range(len(matriz_um[i])):
            outMatriz[i][j] = matriz_um[i][j] + matriz_dois[i][j]
    
    return outMatriz

def escreve_matriz(matrix):
    outputMatrix=''
    for row in matrix:
        for column in row:
            outputMatrix = outputMatrix + str(column) + '\t'
        outputMatrix += '\n'
    
    return outputMatrix

print(escreve_matriz(soma_mat([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]])))
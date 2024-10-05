def escreve_matriz(matrix):
    outputMatrix=''
    for row in matrix:
        for column in row:
            outputMatrix = outputMatrix + str(column) + '\t'
        outputMatrix += '\n'
    
    return outputMatrix

print(escreve_matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))
def elemento_matriz(matrix, row, column):
    if row<0 or row>len(matrix):
        raise ValueError("incide invalido, linha", row)
    elif column<0 or column>len(matrix[row]):
        raise ValueError("indice invalido, coluna", column)
    value = matrix[row][column]

    return value

m = [[1, 2, 3], [4, 5, 6]]
print(elemento_matriz(m, 0, 0))
print(elemento_matriz(m, 0, 3))


#Código do stor
def elemento_matriz(matrix, row, column):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i==row and j==column:
                return matrix[row][column]
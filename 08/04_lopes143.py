#Código do Henrique
def elemento_matriz(matrix, row, column):
    value = (matrix[row])[column]
    #adicionar raise ValueError

    return value

m = [[1, 2, 3], [4, 5, 6]]
print(elemento_matriz(m, 0, 0))
print(elemento_matriz(m, 0, 3))


#Código do stor
def elemento_matriz(matrix, row, column):
    for i in range(len(matrix)):
        for j in range(len(matrix[i]))
        if i == row and j == column:
            return matrix[row][column]


#Outra alternativa do stor
def elemento_matriz(l, r, c):
    if r<0 or r>=len(l):
        raise ...
    elif c<0 or c>len(l[r]):
        raise ...
    
    return l[r][c]
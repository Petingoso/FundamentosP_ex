def soma_mat(matriz1, matriz2):
    r = matriz1
    if len(matriz1) != len(matriz2):
        raise ValueError()
    for i in range(len(matriz1)):
        if len(matriz1[i])!= len(matriz2[i]):
            raise ValueError()
        for j in range(len(matriz1[i])):
            r[i][j] = matriz1[i][j] + matriz2[i][j]
    
    return r

print(soma_mat([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
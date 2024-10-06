# [1  2  3]
# [4  5  6]
#
# [1  4]
# [2  5]
# [3  6]

def transposta(matriz):
    outMatriz = [[0 for i in range(len(matriz))] for i in range(len(matriz[0]))]
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
            outMatriz[coluna][linha] += matriz[linha][coluna]
    
    return outMatriz

print(transposta([[1, 2, 3], [4, 5, 6]]))
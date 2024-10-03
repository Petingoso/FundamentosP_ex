# WARNING: resolução inválida por não fazer proper input checking
def elemento_matriz(m,lin,col):
    if col > len(m): # ultrapassa nº colunas 
        raise ValueError("coluna inválida")
    elif lin>len(m[0]): #ultrapasssa linha qualquer
        raise ValueError("linha inválida")
    return m[col][lin]

m = [[1, 2, 3], [4, 5, 6]]
print(elemento_matriz(m, 0, 0))
print(elemento_matriz(m, 0, 3))

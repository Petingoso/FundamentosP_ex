# Este método chama a função recursivamente quando encontra uma lista num elemento da lista-mãe
def num_occ_lista(lista, numb):
    count=0
    for listElement in lista:
        if isinstance(listElement, list):
            count+=num_occ_lista(listElement, numb)
        elif listElement==numb: #o número não é uma lista
            count+=1
    return count 

print(num_occ_lista([1, 2, 3, 4, 3], 3))
print(num_occ_lista([1, [[[1]], 2], [[[2]]], 2], 2))
def soma_cumulativa(lista):
    outLista = []
    sum = 0
    for i in lista:
        sum += i
        outLista.append(sum)

    return outLista

print(soma_cumulativa([1, 2, 3, 4, 5]))
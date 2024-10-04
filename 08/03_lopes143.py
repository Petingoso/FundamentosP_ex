def soma_cumulativa(list):
    outputList = []
    sum = 0
    for i in list:
        sum += i
        outputList.append(sum)

    return outputList

print(soma_cumulativa([1, 2, 3, 4, 5]))
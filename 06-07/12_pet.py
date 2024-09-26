def apaga1(tup,k):
    i = 0
    for i in range(len(tup)):
        if tup[i] ==k:
            break
    return tup[0:i] + tup[i+1:]
print(apaga1((1, 2, 4, 2, 1), 2))


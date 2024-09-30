def posicoes_maximo(t):
    maxV = t[0]
    output = ()
    if not isinstance(t, tuple):
        raise TypeError('Input não é um tuplo')
    for i in t:
        if i > maxV:
            maxV = i
    for i2 in range(1, len(t)):
        if t[i2] == maxV:
            output += (i2, )

    return output

print(posicoes_maximo((1,2,3,2,1,2,3)))
def codifica(c):
    b=""
    f=""
    for i in range(len(c)):
        if i%2==0:
            b+= c[i]
        else:
            f+= c[i]
    return b+f

print(codifica('abcde'))
# esparguete mas funciona
def reconhece(str):
    letra = ('A','B','C','D')
    # num = (1,2,3,4)
    letters_found=0
    numbers_found=0

    for i in str:
        print(ord(i))
        if (ord(i)>=49 and ord(i)<=52): # ascii 1,2,3,4
            numbers_found = 1
            if not(letters_found): # 111AAAA
                return False
            continue

        if (i not in letra): # n é numero e n e letra
            return False 
        else:
            letters_found = 1

        if (i in letra) and numbers_found: #AA1AA
            return False

    return True

print(reconhece('A1'))
print(reconhece('ABBBBCDDDD23311'))
print(reconhece('ABC12C'))

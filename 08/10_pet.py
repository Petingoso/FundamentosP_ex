import random
# 5 ints por ordem 1->50 
# no repeat 
# 2 estrelas diferentes ordenadas entre 1 e 12
def lista_ord(n,m):
    nums =[]
    num = 0
    i = 0
    while i < n:
        num = int(random.random()*m)+1
        if (num not in nums):
            nums.append(num)
            i +=1
    nums.sort()
    return nums

def euromilhoes():
    nums = lista_ord(5,50)
    estr = lista_ord(2,12)
    return [nums] + [estr]
print(euromilhoes())

def implode1(tup):
    if isinstance(tup,tuple):
        num = 0 
        i=0
        for i in range(len(tup)):
            if not(isinstance(tup[i],int) and 0<=tup[i]<=9):
                raise ValueError("elemento inválido")
            num = num*10 + tup[i]
        return num 
    raise ValueError("tuplo inválido")

def implode2(tup):
    if isinstance(tup,tuple):
        num = 0 
        i=0
        for i in tup:
            if not(isinstance(i,int) and 0<=i<=9):
                raise ValueError("elemento inválido")
            num = num*10 + i
        return num 
    raise ValueError("tuplo inválido")

def implode3(tup):
    if isinstance(tup,tuple):
        num = 0 
        i=0
        while i < len(tup):
            if not(isinstance(tup[i],int) and 0<=tup[i]<=9):
                raise ValueError("elemento inválido")
            num = num*10 + tup[i]
            i+=1
        return num 
    raise ValueError("tuplo inválido")

print(implode1((3,4,0,0,4)))
print(implode2((3,4,0,0,4)))
print(implode3((3,4,0,0,4)))

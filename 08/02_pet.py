# def remove_multiplos1(w,x):
#     i = 0
#     while i<len(w):
#         if (w[i]%x==0):
#             w.remove(w[i])
#             i-=1
#         i+=1
#     return w 
# print(remove_multiplos1([2, 3, 5, 9, 12, 33, 34, 45], 3))

def remove_multiplos1(w,x):
    for i in range(len(w)-1,-1,-1):
        if (w[i]%x==0):
            w.remove(w[i])
    return w 

print(remove_multiplos1([2, 3, 5, 9, 12, 33, 34, 45], 3))

def remove_multiplos2(w,x):
    return [i for i in w if i%x]
print(remove_multiplos2([2, 3, 5, 9, 12, 33, 34, 45], 3))

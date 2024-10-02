def remove_multiplos(w,x):
    i = 0
    while i<len(w):
        if (w[i]%x==0):
            w.remove(w[i])
            i-=1
        i+=1
    return w 
print(remove_multiplos([2, 3, 5, 9, 12, 33, 34, 45], 3))

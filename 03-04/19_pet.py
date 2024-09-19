num = ""
for i in range(1,10):
    num = num + str(i)
    print(eval(num), "x 8 + ", i , "=", (eval(num)*8)+i)

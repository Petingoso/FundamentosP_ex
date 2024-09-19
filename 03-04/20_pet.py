m = eval(input("Diga um num: "))
n = eval(input("Diga um num: "))
curr = 0

times_fit = 0
while True:
        curr = curr + n
        if (curr<=m):
                times_fit +=1
                continue
        break

print(times_fit)

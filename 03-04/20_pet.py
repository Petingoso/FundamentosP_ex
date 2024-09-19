m = eval(input("Diga um num: "))
n = eval(input("Diga um num: "))
curr = n

times_fit = 0
while curr<=m:
        times_fit +=1
        curr = curr + n

print(times_fit)

### algoritmo alternativo
times_fit = 0
while m>=n:
        m-=n
        times_fit +=1
print(times_fit)

num = input("Diga um num: ")
length = len(num)
new_num = num
for i in range(1,length+1):
    new_num = new_num + num[length - i]

print(new_num)


m = eval(input("Introduza o dividendo (m): "))
n = eval(input("Intoduza o divisor (n): "))
q = 0 #Quociente
while m>=n:
    m-=n
    q+=1
print("O valor da divisão inteira é:", q)
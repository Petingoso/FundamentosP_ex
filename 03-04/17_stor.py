num = eval(input("Diga um numero: "))
n_seguidos = 0

while num:
    if num % 100 == 0: # acaba em 00
        n_seguidos +=1
    num//=10
print("O número tem", n_seguidos, "zeros seguidos")

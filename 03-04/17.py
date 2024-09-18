num = input("Diga um numero: ")
n_seguidos = 0

digito_anterior= -1

for i in range(len(num)):
    if(i == 0):
        digito_anterior = num[i]
        pass 

    if(num[i]==0 and digito_anterior==0):
        n_seguidos+=1
    
    digito_anterior = num[i-1]

print("O número tem", n_seguidos, "zeros seguidos")

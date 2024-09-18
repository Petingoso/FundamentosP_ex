num = input("Diga um numero: ")
n_seguidos = 0

digito_anterior= -1

for i in range(0,len(num)):
    if(i == 0):
        digito_anterior = num[i]
        pass 

    # Neste caso estou a trabalhar com strings
    # mas podia ter feito eval(num[i])==0
    if(num[i]=="0" and digito_anterior=="0"): 
        n_seguidos+=1
    
    digito_anterior = num[i]

print("O número tem", n_seguidos, "zeros seguidos")

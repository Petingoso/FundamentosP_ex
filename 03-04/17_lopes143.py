final = 0
count = 0
initNum = eval(input("Escreva um inteiro\n? "))

while initNum!=0:
    digit = initNum%10
    initNum//=10

    if digit==0:
        count+=1
    else:
        count=0
        
    if count>final:
        final=count

if final==1:
    print("O número tem", final,"zero seguido")
else:
    print("O número tem", final,"zeros seguidos")
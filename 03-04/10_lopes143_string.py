initNum = str(input("Escreva um inteiro\n? "))
oddNum = ""

for i in initNum:
    if(eval(i)%2!=0):
        oddNum = oddNum+i

print("Resultado: ", oddNum)

#INFORMAÇÂO
#Nos minitestes não se pode usar for/in com strings
#A pergunta vale com zero
#(ver exercício 10 do Lab03-04)
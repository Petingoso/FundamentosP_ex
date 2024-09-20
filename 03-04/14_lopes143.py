initNum = eval(input("Escreva o número\n? "))
soma = 0

while initNum!=0:
    digit = initNum%10
    initNum//=10
    soma += digit

print("A soma de todos os dígitos é:", soma)
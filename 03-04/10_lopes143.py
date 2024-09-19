x = eval(input("Escreva um inteiro\n? "))
i = 0
output = 0

while x!=0:
    d = x%10
    #o número é lido de frente para trás
    # o d é o último dígito, o resto da divisão por 10
    x//=10
    # o x passa a ser o num. inicial menos o dígito utilizado
    if d%2 !=0:
        #ímpar
        output += d*(10**i)
        #como o núm a adicionaar é da direita para a esquerda,
        #o núm a adicionar vai ser unidade > dezena > centena...
        #o contador i faz isso progressivmente
        #10**0=1, 10**1=10, 10**2=100, ...
        i+=1

print("Resultado: ", output)
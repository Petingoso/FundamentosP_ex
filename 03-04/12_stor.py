# versão sem funções
# como sabemos que o termo inicial é 1
# podemos saber o seguinte sem descobrir fatorais 
# pois termo seguinte é termo_anterior * (x/i)

x = eval(input("Qual o valor de x:"))
n = eval(input("Qual o valor de n:"))

i = 1
soma = 1
termo = 1
while i<=n:
    termo = termo * (x/i)
    soma += termo
    i+=1


print("A soma é:", soma)

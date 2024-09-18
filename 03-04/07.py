horas = eval(input("Quantas horas: "))
salario = eval(input("Qual o salário: ")) #salario/hora
if (horas <= 40):
        ordenado = horas*salario
else:
    ordenado = (40*salario)+ ((horas - 40)*(salario*2))
print (ordenado)


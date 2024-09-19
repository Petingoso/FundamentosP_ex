hour = eval(input("Nº de horas de trabalho numa semana: "))
sal = eval(input("Valor do salário/hora: "))

if hour<=40:
    payment = hour*sal

else:
    payment = (sal*40)+((hour-40)*(2*sal))

print("O ordenado semanal é: ", payment)
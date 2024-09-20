nAlunos = 0
positiva = 0
while True:
    notaInic = eval(input("Introduza a nota do aluno: "))
    if notaInic<0:
        break
    if notaInic>=10:
        positiva +=1
    nAlunos += 1
percent = (positiva/nAlunos)*100
print("Alunos com positiva:", positiva)
print("Nº total de alunos:", nAlunos)
print("Percentagem de positivas:", percent, "%")
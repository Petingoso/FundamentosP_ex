def resumo_FP(dici):
    soma=0
    alunosPos=0
    alunosNeg=0
    for nota in dici:
        numAlunos = len(dici[nota])
        if nota>=10:
            soma += nota*numAlunos
            alunosPos+=numAlunos
        else:
            alunosNeg+=numAlunos

    return ((soma/alunosPos), alunosNeg)

notas_dict = {1 : [46592, 49212, 90300, 59312], 15 : [52592, 59212], 20 : [58323]}

print(resumo_FP(notas_dict))
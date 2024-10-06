from random import random

def euromilhoes():
    numeros = []
    estrelas = []
    n=0
    e=0
    while n<5:
        numtoAdd = int((random()*50)//1)
        if numtoAdd not in numeros:
            numeros.append(numtoAdd)
            n+=1
    while e<2:
        estToAdd = int((random()*12)//1)
        if estToAdd not in estrelas:
            estrelas.append(estToAdd)
            e+=1

    return [sorted(numeros), sorted(estrelas)]

print(euromilhoes())
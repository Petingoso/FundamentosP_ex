# nao funciona mas prova o ponto
from 02_stor import explode,implode
from 04_stor import filtra_pares

def algarismos_pares(n):
    return implode(filtra_pares(explode(n)))
print(algarismos_pares(8927857892))

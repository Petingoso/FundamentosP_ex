def f(x):
     return -(x - 2)**2 + 5



def aproxima(x1,tamanho_intervalo):
    h = (f(x1-tamanho_intervalo) + f(x1))/2
    l = x1 - (x1-tamanho_intervalo)
    return l*h

def aproxima_area(a,b,n):
    dist = (b-a)
    intervalo = (dist)/n
    n_intervalos = int((dist)/intervalo)
    x = a 
    area = 0
    for i in range(n_intervalos):
        x+=intervalo
        area+=aproxima(x,intervalo)
    return area

print(aproxima_area(0.5, 3.5, 6))
print(aproxima_area(0.5, 3.5, 12))
print(aproxima_area(0.5, 3.5, 100))

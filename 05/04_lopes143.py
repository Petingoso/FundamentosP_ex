def area_circulo(r):
    pi = 3.14
    area = (r**2)*pi
    return area

def area_coroa(r1, r2):
    if r1>r2:
        raise ValueError()
    return area_circulo(r2)-area_circulo(r1)

print(area_coroa())
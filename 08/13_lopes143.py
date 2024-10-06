def f(x):
    return -(x-2)**2 + 5

def area_retangulo(left, right):
    comprimento = right-left
    altura = (f(right)+f(left))/2
    return comprimento*altura

def aproxima_area(a, b, n):
    delta= b-a
    interval=delta/n
    area=0
    value_left = a
    value_right = a+interval
    while value_right<=b:
        area+=area_retangulo(value_left, value_right)
        value_right+=interval
        value_left+=interval
    return area

print(aproxima_area(0.5, 3.5, 6))
print(aproxima_area(0.5, 3.5, 12))
print(aproxima_area(0.5, 3.5, 100))
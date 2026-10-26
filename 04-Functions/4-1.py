import math

a=int(input('a='))
b=int(input('b='))
c=int(input('b='))

def pole(a,b,c):
    s = (a+b+c)/2
    wynik = math.sqrt(s*((s-a)+(s-b)+(s-c)))
    return wynik

pole_trojkata=pole(a,b,c)
print(f'Pole trójkąta o bokach {a}, {b}, {c} wynosi {pole_trojkata}')

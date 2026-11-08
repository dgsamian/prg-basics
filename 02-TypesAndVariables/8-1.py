import math
promien = float(input('Podaj promien '))
if promien > 0:
    obwod = 2 * promien * math.pi
    pole = math.pi * math.sqrt(promien)
    print(f'Pole wynosi {round(pole,2)}, obwod wynosi {round(obwod,2)}')
else:
    print('Promien nie moze byc mniejszy niz 1')
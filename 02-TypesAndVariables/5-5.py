cena=float(input('cena='))
promka=float(input('promka w %='))
cena_po=cena - 0.01 * promka * cena
obnizka=cena - cena_po
print(f'Cena po promce wynosi {round(cena_po, 2)}')
print(f'Znizka wynosi {round(obnizka, 2)}')
def month(n):
    miesiac = '' 
    if n==1:
        miesiac = 'Styczeń'
    elif n==2:
        miesiac = 'Luty'
    elif n==3:
        miesiac = 'Marzec' 
    elif n==4:
        miesiac = 'Kwiecień'
    elif n==5:
        miesiac = 'Maj'
    elif n==6:
        miesiac = 'Czerwiec'
    elif n==7:
        miesiac = 'Lipiec'
    elif n==8:
        miesiac = 'Sierpień'
    elif n==9:
        miesiac = 'Wrzesień'
    elif n==10:
        miesiac = 'Październik'
    elif n==11:
        miesiac = 'Listopad'
    elif n==12:
        miesiac = 'Grudzień'
    else:
        miesiac = 'Nie istnieje'

    return miesiac

nr_miesiaca=int(input('Wpisz numer miesiąca: '))
mnth=month(nr_miesiaca)
print(f'Nazwa {nr_miesiaca} miesiąca to {mnth}')


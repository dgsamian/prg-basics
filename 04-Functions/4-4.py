def nazwa_dnia(numer_dnia):
    result = ''
    if numer_dnia == 1:
        result = 'Poniedziałek'
    elif numer_dnia == 2:
        result = 'Wtorek'
    elif numer_dnia == 3:
        result = 'Środa'
    elif numer_dnia == 4:
        result = 'Czwartek'
    elif numer_dnia == 5:
        result = 'Piątek'
    elif numer_dnia == 6:
        result = 'Sobota'
    elif numer_dnia == 7:
        result = 'Niedziela'
    else:
        result = 'Ok'
    return result

dzien_tygodnia=int(input('Który dzień?: '))
tyg=nazwa_dnia(dzien_tygodnia)
print(f'Nazwa {dzien_tygodnia} dnia tygodnia to {tyg}')
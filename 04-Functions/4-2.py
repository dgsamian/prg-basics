def suma_znakow(liczba):
    liczba=abs(liczba)
    tekst=str(liczba)
    total=0

    for znaki in tekst:
        total += int(znaki)

    return total

any_number = int(input('Enter integer number: '))
result = suma_znakow(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')

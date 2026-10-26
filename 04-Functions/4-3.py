def pts_to_grade(points):
    grade = ''
    if points >= 18:
        grade = 'Wspaniale'
    elif points >=14:
        grade = 'Dobrze'
    elif points >=10:
        grade = 'Dostatecznie'
    else:
        grade = 'Ndst'
    return grade

wynik=int(input('Ile pkt: '))
final_grade = pts_to_grade(wynik)
print(f'Zdobyłeś {wynik} punktów na teście. Twoja ocena to {final_grade}')
# Exercise 2
# Classification Of Students

ClassGrades = {
    'A': [],
    'B': [],
    'C': [],
    'D': [],
    'E': [],
    'F': []
}

while True:
    Grade = int(input('Student\'s grade (0-100): '))
    if Grade >= 90:
        ClassGrades['A'].append(Grade)
    elif Grade >= 70:
        ClassGrades['B'].append(Grade)
    elif Grade >= 60:
        ClassGrades['C'].append(Grade)
    elif Grade >= 50:
        ClassGrades['D'].append(Grade)
    else:
        ClassGrades['F'].append(Grade)
    if input('Continue? (y/n) : ') == 'n':
        break

print(ClassGrades)

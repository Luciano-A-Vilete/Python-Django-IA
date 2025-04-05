students = ["Joseph", "Brigham", "Lorenzo", "Wilford", "John"]

favorite_numbers = (3, 7, 15, 156, 418)

grades = {
    "Joseph": 90,
    "Brigham": 100,
    "Lorenzo": 85,
    "Wilford": 95,
    "John": 92
}

print('Students grades: ')
for student, grade in grades.items():
    print(f'{student} {grade}')
    
magna_cum_laude = [student for student, grade in grades.items() if grade >= 95]
print('Magna cum laude Students (grade >= 95): ', magna_cum_laude)
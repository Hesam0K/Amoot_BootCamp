# Problem 2
# Analysis of Students grades

StudentData = {
    'Alice': {
        'Math': 70,
        'English': 60,
        'Science': 80
    },
    'Bob': {
        'Math': 48,
        'English': 45,
        'Science': 20
    },
    'charlie': {
        'Math': 50,
        'English': 55,
        'Science': 65
    }
}

bestStudent = ['NoName', 0]  # [name, Average Grade]
worstStudent = ['NonName', 100]  # [name, Average Grade]
failedStudents = []  # is going to record multiple students

for s in StudentData:
    failingFlag = True  # every body fails unless the opposite is proved!
    averageGrade = 0
    for i in StudentData[s]:
        averageGrade += StudentData[s][i]  # sum += grade
        if StudentData[s][i] >= 50:  # condition of passing!
            failingFlag = False
    averageGrade /= len(StudentData[s])  # average = sum / number

    if averageGrade > bestStudent[1]:  # is this student the best?
        bestStudent[0] = s
        bestStudent[1] = averageGrade
    if averageGrade < worstStudent[1]:  # is this student the worst?
        worstStudent[0] = s
        worstStudent[1] = averageGrade
    if failingFlag:  # recording the failed student
        failedStudents.append(s)

print(f"Highest average grade: {bestStudent[0]} ({bestStudent[1]:.2f})")
print(f"Lowest average grade: {worstStudent[0]} ({worstStudent[1]:.2f})")
print("Students failing: ", failedStudents)

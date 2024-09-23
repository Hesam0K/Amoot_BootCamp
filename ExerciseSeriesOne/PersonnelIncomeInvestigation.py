# Problem3
# Personnel Income Investigation System

import math  # for inf

Employees = {
    'john': {
        'department': 'Engineering',
        'salary': 70000
    },
    'Jane': {
        'department': 'HR',
        'salary': 65000
    },
    'Mike': {
        'department': 'Engineering',
        'salary': 75000
    },
    'Anna': {
        'department': 'Marketing',
        'salary': 60000
    },
    'Tom': {
        'department': 'HR',
        'salary': 67000
    }
}

user_departments = input('Enter departments to investigate: '
                         'in form of (department1 department2 etc)\n').split()
theRichestDepartment = ['NoName', 0]
thePoorestDepartment = ['NoName', math.inf]
for ud in user_departments:
    averageSalary = 0
    count = 0
    for E in Employees:
        if Employees[E]['department'] == ud:
            averageSalary += Employees[E]['salary']  # sum += money
            count += 1
    averageSalary /= count  # sum / number

    if averageSalary > theRichestDepartment[1]:  # is this the richest department?
        theRichestDepartment[0] = ud
        theRichestDepartment[1] = averageSalary
    if averageSalary < thePoorestDepartment[1]:  # is this the Poorest department?
        thePoorestDepartment[0] = ud
        thePoorestDepartment[1] = averageSalary

    print('Department', ud, ':')
    print(f'Average Salary: {averageSalary:.0f}')
print('Department with highest average salary: ')
print(f'{theRichestDepartment[0]} ({theRichestDepartment[1]:.0f})')
print('Department with lowest average salary: ')
print(f'{thePoorestDepartment[0]} ({thePoorestDepartment[1]:.0f})')

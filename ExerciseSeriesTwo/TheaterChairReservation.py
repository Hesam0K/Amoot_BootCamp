# Problem 1
# Theater chair rezervation system

def build_theater(row=5, column=5):  # builds a (row * column) theater with empty seats
    theater = []
    for i in range(row):
        theater_row = []
        for j in range(column):
            theater_row.append(0)
        theater.append(theater_row)
    return theater


def show_theater(theater):  # shows the theater with tagged rows and columns
    print(' ', end=' ')
    for x in range(1, len(theater[0]) + 1):
        print(x, end=' ')  # printing column tags
    print()
    for i in range(len(theater)):
        print(chr(97 + i), end=' ')  # printing row tags
        for j in range(len(theater[i])):
            print(theater[i][j], end=' ')
        print()


def reserve_chair(theater, row, column):
    if row < 0 or row > len(theater):
        print('Invalid row. try again!')
        return False
    elif column < 0 or column > len(theater[0]):
        print('Invalid column. try again!')
        return False
    elif theater[row][column] == 1:
        print('this chair is reserved! try again!')
        return False
    else:
        print(f'Selected chair is successfully reserved! your chair is {chr(97 + row)}_{column + 1}')
        theater[row][column] = 1
        return True


def user_reserves_chair(theater):
    while True:
        chair_address = input('Enter chair address to reserve: (example: "a_1")\n').split('_')
        is_done = reserve_chair(theater, ord(chair_address[0]) - 97, int(chair_address[1]) - 1)
        if is_done:
            print('state of theater after your reservation is:')
            show_theater(theater)
            break
# ===============================================================================================


theater = build_theater()
print('Current state of theater is:')
show_theater(theater)
n = int(input('How many chairs do you want to reserve: '))
for i in range(n):
    user_reserves_chair(theater)

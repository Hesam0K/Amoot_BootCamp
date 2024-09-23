# Exercise 1
# Sum of odd and even numbers from 0 to 100

oddSum = 0
evenSum = 0
for i in range(0, 101):
    if i % 2 == 0:
        evenSum += i
    else:
        oddSum += i
print(f'Sum of even numbers from 0 to 100: {evenSum}')
print(f'Sum of odd numbers from 0 to 100: {oddSum}')
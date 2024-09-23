# Exercise 3
# Do you have my fruit

fruitList = ['apple', 'banana', 'orange']

user_fruit = input('Enter your desired fruit: ')
if user_fruit in fruitList:
    print('Entered fruit is in the fruit list!')
else:
    fruitList.append(user_fruit)
    print(f'{user_fruit} is added to the fruit list.')

print(f'fruit list: {fruitList}')
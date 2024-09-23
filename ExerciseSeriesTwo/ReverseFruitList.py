# Exercise 3
# Reverse the fruit list

fruits = ['apple', 'banana', 'orange', 'cherry', 'grape']

# fruits.reverse()

x = 0  # moves from start to middle
y = len(fruits) - 1  # moves from end to middle

while x < y:
    temp = fruits[x]  # temporary valuable for swap
    fruits[x] = fruits[y]
    fruits[y] = temp

    x += 1  # movements
    y -= 1
print(fruits)

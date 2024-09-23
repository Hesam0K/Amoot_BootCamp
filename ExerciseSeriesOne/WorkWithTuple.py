# Exercise 5
# Work with tuple

fruit = ('apple', 'banana', 'cherry')
food = ('chicken', 'fish', 'meat')
drink = ('tea', 'coffee', 'milk')

edible_union = fruit + food + drink
print(f"edible union : {edible_union}")

edible_union += ('peach',)  # single appending
edible_union += ('pasta', 'soda')  # join tuples
print(f"edible union + favorites : {edible_union}")

favorites = list(edible_union[-3:])
print(f"My favorites : {favorites}")
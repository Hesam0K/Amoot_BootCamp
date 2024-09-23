# Exercise 1
# Dict a Person

Person = {
    'first_name': 'Ehsan',
    'last_name': 'Hosseini',
    'age': 25,
    'country': 'iran',
    'is_married': True,
    'skills': ['JavaScript', 'Django', 'Odoo', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'postal_code': '02210'
    }
}

# does the Person have "skills" key? -> print first, last and middle skills.

if 'skills' in Person:
    print(Person['skills'][0],
          Person['skills'][len(Person['skills']) - 1],
          Person['skills'][len(Person['skills']) // 2])

# print info with fstring
print(f"{Person['first_name']} {Person['last_name']} lives in {Person['country']}. "
      f"he is {'married. ' if Person['is_married'] else 'single. '}"
      f"he has these skills: {Person['skills']}")
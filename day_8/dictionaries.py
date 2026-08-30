    # Create an empty dictionary named dog.
dog = {}

    # Add name, color, breed, legs, and age to the dog dictionary.
dog['name'] = 'cola'
dog['color'] = 'brown'
dog['breed'] = 'zato'
dog['legs'] = 4
dog['age'] = 3
print(dog)

    # Create a student dictionary with first_name, last_name, gender, age, marital_status, skills, country, city, and address as keys.
student = {
    'first_name': 'Freddy',
    'last_name': 'Rosa',
    'gender': 'Male',
    'age': 32,
    'marital_status': 'married',
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'country': 'Puerto Rico',
    'city': 'Caguas',
    'address': 'Aymaco'
}
print(student)

    # Find the length of the student dictionary.
print(len(student))

    # Get the value of skills and check its data type. It should be a list.
print(student['skills'])
print(type(student['skills']))

    # Modify the skills value by adding one or two skills.
student['skills'].append('GO')
student['skills'].append('SQL')
print(student)

    # Get the dictionary keys as a list.
keys = student.keys()
print(list(keys))

    # Get the dictionary values as a list.
value = student.values()
print(list(value))

    # Convert the dictionary into a list of tuples using the items() method.
lst = student.items()
print(list(lst))

    # Delete one item from the dictionary.
student.pop('skills')
print(student)

    # Delete one of the dictionaries completely.
del student

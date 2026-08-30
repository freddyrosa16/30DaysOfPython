    # Ask the user to enter their age. If they are 18 or older, tell them they are old enough to learn to drive. Otherwise, calculate and display how many more years they must wait.
age = int(input('Enter age: '))
if age >= 18:
    print('You are old enough to drive.')
else:
    print(f'You must wait {18 - age} years to be able to drive.')

    # Compare my_age with an age entered by the user. Explain who is older, handle equal ages, and use "year" for a difference of one or "years" for larger differences.
my_age = 32
if my_age == age:
    print('We are the same age.')

    # Ask the user for two numbers. Display whether the first number is greater than, smaller than, or equal to the second number.


    # Ask for a student's score and display the corresponding grade:
        # 90-100: A
        # 80-89: B
        # 70-79: C
        # 60-69: D
        # 0-59: F


    # Ask the user for a month and display its season:
        # September, October, November: Autumn
        # December, January, February: Winter
        # March, April, May: Spring
        # June, July, August: Summer


    # Use this fruit list and check a chosen fruit:
        # fruits = ['banana', 'orange', 'mango', 'lemon']
        # If the fruit is not in the list, add it and display the modified list.
        # If it is already present, display that the fruit already exists in the list.


    # Use this person dictionary for the following exercises. You may modify it:
        # person = {
        #     'first_name': 'Asabeneh',
        #     'last_name': 'Yetayeh',
        #     'age': 250,
        #     'country': 'Finland',
        #     'is_married': True,
        #     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        #     'address': {
        #         'street': 'Space street',
        #         'zipcode': '02210'
        #     }
        # }


    # Check whether person contains the skills key. If it does, display the middle skill from the skills list.


    # Check whether person contains the skills key. If it does, check whether Python is one of the person's skills and display the result.


    # Determine the person's developer title from their skills:
        # If the skills are only JavaScript and React, display "He is a front end developer".
        # If the skills include Node, Python, and MongoDB, display "He is a backend developer".
        # If the skills include React, Node, and MongoDB, display "He is a fullstack developer".
        # Otherwise, display "unknown title".


    # If the person is married and lives in Finland, display this information using their name and country:
        # Asabeneh Yetayeh lives in Finland. He is married.

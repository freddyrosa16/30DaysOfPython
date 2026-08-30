    # Ask the user to enter their age. If they are 18 or older, tell them they are old enough to learn to drive. Otherwise, calculate and display how many more years they must wait.
age = int(input('Enter age: '))
if age >= 18:
    print('You are old enough to drive.')
else:
    print(f'You must wait {18 - age} years to be able to drive.')

    # Compare my_age with an age entered by the user. Explain who is older, handle equal ages, and use "year" for a difference of one or "years" for larger differences.
my_age = 32
difference = my_age - age

if difference == 0:
    print('We are the same age.')
elif difference == 1:
    print(f'I am older by {difference} year.')
elif difference > 1:
    print(f'I am older by {difference} years.')
elif difference == -1:
    print(f'You are older by {abs(difference)} year.')
elif difference < -1:
    print(f'You are older by {abs(difference)} years.')

    # Ask the user for two numbers. Display whether the first number is greater than, smaller than, or equal to the second number.
first_number = int(input('Enter a number: '))
second_number = int(input('Enter a second number: '))

if first_number > second_number:
    print(f'First Number {first_number} is greater than Second Number {second_number}')
elif first_number < second_number:
    print(f'First Number {first_number} is smaller than Second Number {second_number}')
else:
    print(f'First Number {first_number} is equal to {second_number}')

    # Ask for a student's score and display the corresponding grade:
        # 90-100: A
        # 80-89: B
        # 70-79: C
        # 60-69: D
        # 0-59: F
score = int(input('Enter your score: '))
if score >= 90 and score <= 100:
    print('You have an A.')
elif score >= 80 and score <= 89:
    print('You have a B.')
elif score >= 70 and score <= 79:
    print('You have a C.')
elif score >= 60 and score <= 69:
    print('You have a D.')
elif score >= 0 and score <= 59:
    print('You have an F.')

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

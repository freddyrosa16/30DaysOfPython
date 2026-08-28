import math


    # Area of a triangle
base = int(input("Enter the base of the triangle: "))
height = int(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print(area)

    # Perimeter of a triangle
side_a = int(input("Enter side a of the triangle: "))
side_b = int(input("Enter side b of the triangle: "))
side_c = int(input("Enter side c of the triangle: "))
perimeter = side_a + side_b + side_c
print(perimeter)

    # Area and Perimeter of a Rectangle
length = int(input("Enter the length of the Rectangle: "))
height = int(input("Enter the height of the Rectangle: "))
area = length * height
perimeter = 2 * (length + height)
print(area, perimeter)

    # Area and Circumference of a Circle
pi = 3.14
radius = int(input("Enter the radius of the circle: "))
area = pi * radius * radius
circumference = 2 * pi * radius
print(area, circumference)

    # Find the slope, x-intercept and y-intercept of y = 2x -2
slope_1 = 2

# Y Intercept
x = 0
y_intercept = (slope_1 * x) - 2

# X Intercept
x_intercept = (0 - y_intercept) / slope_1
print(slope_1, x_intercept, y_intercept)

    # Find slope m = y2-y1/x2-x1 and Euclidean distance between point (2, 2) and point (6,10)
slope_2 = (10 - 2) / (6 - 2)
euclidean = math.dist((2, 2), (6, 10))
print(slope_2, euclidean)

    # Comparing slopes
print(slope_1 == slope_2)

    # Calculate the value of y (y = x^2 + 6x + 9) using different x values that make y = 0
x = -3
y = ((-3) ** 2) + (6 * -3) + 9
print(y)

    # Find the length of 'python' and 'dragon' and make a falsy comparison statement.
python = len('python')
dragon = len('dragon')
print(python != dragon)

    # Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

    # Use in operator to check if jargon is in the sentence.
print('jargon' in 'I hope this course is not full of jargon')

    # Use and operator to check that there is no 'on' is found in both 'python' and 'dragon'
print('on' not in 'python' and 'on' not in 'dragon')

    # Find the length of the text python and convert the value to float and convert it to string
python = str(float(len('python')))
print(python)

    # I check if a number is even using n % 2 == 0.

# The % operator returns the remainder after dividing n by 2.
# If the remainder is 0, the number is divisible by 2, so it is even.

# For example:
# 8 // 2 = 4 complete groups
# 8 % 2 = 0 objects left over

# | . . | . . | . . | . . |

# There is no extra dot outside the four groups.
# Therefore, the remainder is 0, and 8 is even.

# With 9:
# 9 // 2 = 4 complete groups
# 9 % 2 = 1 object left over

# | . . | . . | . . | . . | .

# There is one dot outside the four complete groups.
# Therefore, the remainder is 1, and 9 is odd.

    # Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7 // 3 == int(2.7))

    # Check if type of '10' is equal to type of 10
print(type('10') == type(10))

    # Check if int('9.8') is equal to 10
print(int(float("9.8")) == 10)

    # Prompt the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input('Enter the hours worked per week: '))
rate = int(input('Enter the rate per hour: '))
weekly = hours * rate
pay = hours * rate * 52 / 12
print(f'Your weekly rate is of {weekly}')
print(f'Your monthly rate is of {pay}')

    # Prompt the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input('Enter the number of years you have lived: '))
seconds = 3600 * years * 365 * 24 * 60 * 60
print(f'You have lived for {seconds} seconds')

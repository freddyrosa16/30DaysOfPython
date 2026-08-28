    # Day 2: 30 Days of python programming
first_name = 'Freddy'
last_name = 'Rosa'
full_name = 'Freddy Rosa'
country = 'Puerto Rico'
city = 'Caguas'
age = 32
year = 2026
is_married = True
is_true = True
is_light_on = False
i, j, k = 1, 'no', False

    # Checking the data types
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(i), type(j) ,type(k))

    # Finding the length of the first_name and last_name
print(len(first_name)) # 6
print(len(last_name)) # 4
# First name is longer by 2 characters

# new variables (int)
num_one = 5
num_two = 4

# addition
sum = num_one + num_two
print(sum)

# substraction
substraction = num_two - num_one
print(substraction)

# multiplication
multiplication = num_two * num_one
print(multiplication)

# division
division = num_two / num_one
print(division)

# modulo remainder
remainder = num_two % num_one
print(remainder)

# exponential
exp = num_one ** num_two
print(exp)

# floor division
floor_division = num_one // num_two
print(floor_division)

# The radius of a circle is 30 meters.
radius = 30
pi = 3.14
area_of_circle = pi * (radius ** 2)
print(area_of_circle)

circum_of_circle = 2 * pi * radius
print(circum_of_circle)

user_radius = float(input("Enter the radius: "))
print(pi * (user_radius ** 2))

# Storing value of the corresponding variable name
new_first_name = input("Please provide your first name: ")
new_last_name = input("Please provide your last name: ")
new_country = input("Please provide the country you live in: ")
new_age = int(input("Please provide your age: "))

user = {
    "first name": new_first_name,
    "last name": new_last_name,
    "country": new_country,
    "age": new_age,
}
print(user)

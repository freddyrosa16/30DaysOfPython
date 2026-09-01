# Day 11: Functions

# Exercises: Level 1

# 1. Define add_two_numbers with two parameters. Return their sum.
def add_two_numbers(a, b):
    return a + b
print(add_two_numbers(3, 5))

# 2. Define area_of_circle. Accept a radius and return the circle's area.
# Formula: area = pi * radius * radius
def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area
print(area_of_circle(5))

# 3. Define add_all_nums so it can accept any number of arguments and return their total.
# Validate that every argument is a number. If one is not numeric, return helpful feedback.
def add_all_nums(*args):
    total = 0
    for i in args:
        if isinstance(i, int) or isinstance(i, float):
            total += i
        else:
            return 'The arguments should be an int or float'
    return total
print(add_all_nums(1, 2.5, 3, 4))

# 4. Define convert_celsius_to_fahrenheit and return the converted temperature.
# Formula: Fahrenheit = (Celsius * 9 / 5) + 32
def convert_celsius_to_farenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit
print(convert_celsius_to_farenheit(20))

# 5. Define check_season. Accept a month and return Autumn, Winter, Spring, or Summer.
def check_season(month):
    autumn = ['September', 'October', 'November']
    winter = ['December', 'January', 'February']
    spring = ['March', 'April', 'May']
    summer = ['June', 'July', 'August']
    if month in autumn:
        return 'Autumn'
    elif month in winter:
        return 'Winter'
    elif month in spring:
        return 'Spring'
    elif month in summer:
        return 'Summer'
actual_month = input('Enter the month: ')
print(check_season(actual_month))

# 6. Define calculate_slope and return the slope of a linear equation.
def calculate_slope(x1, x2, y1, y2):
    if x2 == x1:
        return None
    return (y2 - y1) / (x2 - x1)
slope = calculate_slope(1, 2, 3, 4)
print(slope)

# 7. Define solve_quadratic_eqn. Accept the values needed for ax^2 + bx + c = 0
# and return the equation's solution or solutions.
def solve_quadratic_eqn(a, b, c):
    if a == 0:
        return None
    discriminant = (b ** 2) - (4 * a * c)
    if discriminant < 0:
        return None
    square_root = discriminant ** 0.5
    x1 = ((-b) - square_root) / (2 * a)
    x2 = ((-b) + square_root) / (2 * a)
    return x1, x2
print(solve_quadratic_eqn(1, -3, 2))


# 8. Define print_list. Accept a list and print each item individually.
def print_list():
    lst = ['NVIDIA', 'APPLE', 'OPENAI', 'SAMSUNG']
    for i in lst:
        print(i)
print_list()

# 9. Define reverse_list. Accept a list and return a new list in reverse order using a loop.
# Expected examples:
# reverse_list([1, 2, 3, 4, 5]) returns [5, 4, 3, 2, 1]
# reverse_list(['A', 'B', 'C']) returns ['C', 'B', 'A']
def reverse_list(lst):
    new_list = []
    for i in lst:
        new_list.insert(0, i)
    return new_list
print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(['A', 'B', 'C']))


# 10. Define capitalize_list_items. Accept a list and return a new list whose items are capitalized.
def capitalize_list_items(lst):
    new_lst = []
    for i in lst:
        new_lst.append(i.capitalize())
    return new_lst
print(capitalize_list_items(['hello', 'my', 'name', 'is', 'freddy']))

# 11. Define add_item. Accept a list and an item, then return the list with that item added at the end.
# Expected examples:
# add_item(['Potato', 'Tomato', 'Mango', 'Milk'], 'Meat')
# returns ['Potato', 'Tomato', 'Mango', 'Milk', 'Meat']
# add_item([2, 3, 7, 9], 5) returns [2, 3, 7, 9, 5]
def add_item(lst, item):
    lst.append(item)
    return lst
print(add_item(['Potato', 'Tomato', 'Mango', 'Milk'], 'Meat'))
print(add_item([2, 3, 7, 9], 5))

# 12. Define remove_item. Accept a list and an item, then return the list without that item.
# Expected examples:
# remove_item(['Potato', 'Tomato', 'Mango', 'Milk'], 'Mango')
# returns ['Potato', 'Tomato', 'Milk']
# remove_item([2, 3, 7, 9], 3) returns [2, 7, 9]
def remove_item(lst, item):
    for i in lst:
        if i == item:
            lst.remove(i)
    return lst
print(remove_item(['Potato', 'Tomato', 'Mango', 'Milk'], 'Mango'))
print(remove_item([2, 3, 7, 9], 3))

# 13. Define sum_of_numbers. Accept a number and return the sum from 0 through that number.
# Expected results: sum_of_numbers(5) returns 15, sum_of_numbers(10) returns 55,
# and sum_of_numbers(100) returns 5050.
def sum_of_numbers(num):
    total = 0
    for i in range(0, num + 1):
        total += i
    return total
print(sum_of_numbers(100))

# 14. Define sum_of_odds. Accept a number and return the sum of all odd numbers through it.
def sum_of_odds(a):
    total = 0
    for i in range(1, a + 1, 2):
        total += i
    return total
print(sum_of_odds(100))

# 15. Define sum_of_even. Accept a number and return the sum of all even numbers through it.
def sum_of_even(a):
    total = 0
    for i in range(0, a + 1, 2):
        total += i
    return total
print(sum_of_even(100))


# Exercises: Level 2

# 1. Define evens_and_odds. Accept a positive integer and count the even and odd numbers
# from 0 through that integer. For 100, there should be 51 evens and 50 odds.
def even_and_odds(a):
    even = 0
    odd = 0
    for i in range(0, a + 1):
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)
print(even_and_odds(100))

# 2. Define factorial. Accept a whole number and return its factorial.
def factorial(a):
    total = 1
    if a <= 0:
        return None
    for i in range(1, a + 1):
        total *= i
    return total
print(factorial(5))

# 3. Define is_empty. Accept a value and determine whether it is empty.
def is_empty(value):
    if len(value) == 0:
        return True
    return False
print(is_empty([]))

# 4. Define separate functions that accept a list of numbers and calculate its:
# mean, median, mode, range, variance, and standard deviation.
def calculate_mean(lst):
    length = len(lst)
    sum_of_numbers = 0
    for i in lst:
        sum_of_numbers += i
    mean = sum_of_numbers / length
    return mean
print(calculate_mean([1,2,2,5]))

def calculate_median(lst):
    length = len(lst)
    new_sorted_lst = sorted(lst)
    mid = length // 2
    if length % 2 == 1:
        return new_sorted_lst[mid]
    else:
        return new_sorted_lst[mid - 1]
print(calculate_median([1,2,3,4]))

def calculate_mode(lst):
    new_dict_mode = {}
    for i in lst:
        if i not in new_dict_mode:
            new_dict_mode[i] = 1
        else:
            new_dict_mode[i] += 1
    sorted_dict = sorted(new_dict_mode.items(),reverse=True, key=lambda x: x[1])
    return sorted_dict[0][0]
print(calculate_mode([1,2,3,4,4,4,5,5,6,6,7,7,7,7,8,8,8,9,9,9]))

def calculate_range(lst):
    total = 0
    new_sorted_range = sorted(lst, reverse=True)
    total = new_sorted_range[0] - new_sorted_range[-1]
    return total
print(calculate_range([1,2,3,4,2,5,1,2,9,7]))

def calculate_variance(lst):
    mean = calculate_mean(lst)
    length = len(lst)
    variance = 0
    for i in lst:
        distance = (i - mean) ** 2
        variance += distance
    variance = variance / length
    return variance
print(calculate_variance([1,2,3,4,2,5,1,2,9,7]))

def calculate_standard_deviation(lst):
    variance = calculate_variance(lst)
    std_dev = variance ** 0.5
    return std_dev
print(calculate_standard_deviation([1,2,3,4,2,5,1,2,9,7]))

# 5. Define greet with a default name argument. With no supplied name, return or print
# "Hello, Guest!" With a supplied name, greet that person instead.
def greet(name='Guest'):
    return f'Hello, {name}!'
print(greet(name='Freddy'))

# 6. Define show_args so it accepts any number of named arguments and prints each name and value.
# Example inputs may include name='Alice', age=30, and city='New York'.
def show_args(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')
show_args(name="Alice", age=30, city="New York")


# Exercises: Level 3

# 1. Define is_prime. Accept a number and return whether it is prime.

# 2. Define a function that accepts a list and checks whether every item is unique.

# 3. Define a function that accepts a list and checks whether all items have the same data type.

# 4. Define a function that checks whether a provided name is a valid Python variable name.

# 5. Use data/countries_data.py to define most_spoken_languages.
# It should accept whether the caller wants 10 or 20 results and return that many languages
# in descending order of frequency.

# 6. Use data/countries_data.py to define most_populated_countries.
# It should accept whether the caller wants 10 or 20 results and return that many countries
# in descending order of population.

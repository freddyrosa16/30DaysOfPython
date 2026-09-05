# Day 13: List Comprehension

# Exercises

# 1. Using list comprehension, make a new list that keeps only the negative numbers and zero from this list:
# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
def filtered():
    numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
    filtered_lst = list(filter(lambda x: x <= 0, numbers))
    return filtered_lst
print(filtered())

# 2. Using list comprehension, flatten this list of lists into one list:
# list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
def flatten():
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened_list =[ number for row in list_of_lists for number in row]
    return flattened_list
print(flatten())

# 3. Using list comprehension, create this list of tuples for the numbers from 0 through 10:
# [(0, 1, 0, 0, 0, 0, 0),
#  (1, 1, 1, 1, 1, 1, 1),
#  (2, 1, 2, 4, 8, 16, 32),
#  (3, 1, 3, 9, 27, 81, 243),
#  (4, 1, 4, 16, 64, 256, 1024),
#  (5, 1, 5, 25, 125, 625, 3125),
#  (6, 1, 6, 36, 216, 1296, 7776),
#  (7, 1, 7, 49, 343, 2401, 16807),
#  (8, 1, 8, 64, 512, 4096, 32768),
#  (9, 1, 9, 81, 729, 6561, 59049),
#  (10, 1, 10, 100, 1000, 10000, 100000)]
def create_list_tp():
    num = [(i, 1, i, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11)]
    return num
print(create_list_tp())

# 4. Using list comprehension, change this country data into the expected list below:
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')],
#              [('Norway', 'Oslo')]]
# Expected output:
# [['FINLAND', 'FIN', 'HELSINKI'],
#  ['SWEDEN', 'SWE', 'STOCKHOLM'],
#  ['NORWAY', 'NOR', 'OSLO']]
def country_list():
    countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
    country = [[j[0].upper(), j[0][:3].upper(), j[1].upper()] for i in countries for j in i]
    return country
print(country_list())

# 5. Using list comprehension, change this country data into a list of dictionaries:
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')],
#              [('Norway', 'Oslo')]]
# Expected output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
#  {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
#  {'country': 'NORWAY', 'city': 'OSLO'}]


# 6. Using list comprehension, change this list of names into a list of full-name strings:
# names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')],
#          [('Donald', 'Trump')], [('Bill', 'Gates')]]
# Expected output:
# ['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']


# 7. Write a lambda function that calculates either the slope or the y-intercept of a linear function.

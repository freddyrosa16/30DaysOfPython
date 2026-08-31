from data.countries import countries
from data.countries_data import countries_data


# 1. Print the numbers from 0 through 10 with a for loop. Then do the same with a while loop.
for i in range(0, 11):
    print(i)

i = 0
while i < 11:
    print(i)
    i += 1

# 2. Print the numbers from 10 down to 0 with a for loop. Then do the same with a while loop.
for i in range(10, 0 - 1, -1):
    print(i)

i = 10
while i >= 0:
    print(i)
    i -= 1

# 3. Use a loop and seven print calls to create this triangle:
# #
# ##
# ###
# ####
# #####
# ######
# #######
for i in range(1, 8):
    print('#' * i)

# 4. Use nested loops to create an 8-by-8 square made of # symbols.
for i in range(1, 9):
    for j in range(1, 9):
        print('#', end=' ')
    print()


# 5. Print the square of every number from 0 through 10 in this format:
# number x number = result
number = 0
for i in range(0, 11):
    print(f'{number} x {number} = {number * number}')
    number += 1


# 6. Use a for loop to print every item in this list:
# ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
frameworks = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for i in frameworks:
    print(i)

# 7. Loop from 0 through 100 and print only the even numbers.
for i in range(0, 101, 2):
    print(i)

# 8. Loop from 0 through 100 and print only the odd numbers.
for j in range(1, 101, 2):
    print(j)


# 1. Loop from 0 through 100, add every number, and print the total.
# Expected total: 5050
total = 0
for i in range(0, 101):
    total += i
print(total)

# 2. Loop from 0 through 100 and calculate two separate totals:
# one for the even numbers and one for the odd numbers.
# Expected even total: 2550
# Expected odd total: 2500
even = 0
odd = 0
for i in range(0, 101, 2):
    even += i
print(even)
for j in range(1, 101, 2):
    odd += j
print(odd)

# 1. Use the countries list from the course's countries.py data file.
# Print every country whose name contains the word "land".
for i in countries:
    if 'land' in i:
        print(i)

# 2. Reverse this fruit list using a loop:
# ['banana', 'orange', 'mango', 'lemon']
fruit = []
fruits = ['banana', 'orange', 'mango', 'lemon']
for i in fruits[::-1]:
    fruit.append(i)
print(fruit)

# 3. Use the course's countries_data.py data file to answer these questions:
# - How many unique languages are represented?
# - What are the ten most widely spoken languages?
# - What are the ten most populated countries?
unique_languages = 0
languages = set()
for country in countries_data:
    for language in country['languages']:
        languages.add(language)
unique_languages = len(languages)
print(unique_languages)

most_languages = {}
for country in countries_data:
    for language in country['languages']:
        if language not in most_languages:
            most_languages[language] = 1
        else:
            most_languages[language] += 1
new_sort = sorted(most_languages.items(), reverse=True, key=lambda x: x[1])
print(new_sort[:10])

total = []
for i in countries_data:
    total.append((i['population'], i['name']))
new_sort_tp = sorted(total, reverse=True)
print(new_sort_tp[:10])

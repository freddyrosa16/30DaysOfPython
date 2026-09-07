# Starting lists for Levels 1 and 2, unless an exercise asks for the full country list:
from functools import reduce


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exercises: Level 1

# 1. Explain how map, filter, and reduce differ from one another.
# Map applies a function to each item in an iterable and returns an iterator of the results; map itself does not change the original iterable.
# Filter applies a condition function to each item in an iterable and returns an iterator containing only the items that satisfy the condition.
# Reduce repeatedly applies a function to combine the accumulated result with the next item in an iterable, producing one final result.

# 2. Explain what higher-order functions, closures, and decorators do and how they differ.
# Decorator allows the user to add a functionality to the existing object without modifying the structure
# Closures allow the nested function access the outer function
# higher-order function takes another function as an input and returns a function or both

# 3. Define a named function, then pass it to map, filter, or reduce as the callback, following the lesson examples.
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))

# 4. Print every country from the countries list using a for loop.
for country in countries:
    print(country)

# 5. Print every name from the names list using a for loop.
for name in names:
    print(name)

# 6. Print every number from the numbers list using a for loop.
for number in numbers:
    print(number)

# Exercises: Level 2

# 1. Apply map to the countries list to produce a new list of uppercase country names.
upper_country = list(map(lambda x: x.upper(), countries))
print(upper_country)

# 2. Apply map to the numbers list to produce a new list containing each number squared.
squared_number = list(map(lambda x: x ** 2, numbers))
print(squared_number)

# 3. Apply map to the names list to produce a new list of uppercase names.
upper_name = list(map(lambda x: x.upper(), names))
print(upper_name)
# 4. Apply filter to keep the country names containing 'land'.
filter_land = list(filter(lambda x: 'land' in x, countries))
print(filter_land)

# 5. Apply filter to keep the country names with exactly six characters.
names_6_characters = list(filter(lambda x: len(x) == 6, names))
print(names_6_characters)

# 6. Apply filter to keep the country names with six or more characters.
filter_countries = list(filter(lambda x: len(x) >= 6, countries))
print(filter_countries)

# 7. Apply filter to keep the country names beginning with 'E'.
countries_start_e = list(filter(lambda x: x.startswith('E'), countries))
print(countries_start_e)

# 8. Combine at least two operations from map, filter, and reduce in one chain, passing one operation's output into the next using Python syntax.
print(list(map(lambda x: x.upper(), filter(lambda x: x.endswith('land'), countries))))

# 9. Define get_string_lists to accept a list and return a new list containing only its string values.
def get_string_lists(lst):
    strings_in_a_list = list(filter(lambda x: isinstance(x, str), lst))
    return strings_in_a_list
print(['OpenAI', 'NVIDIA', 16, 4.0, True])

# 10. Apply reduce to calculate the total of the numbers list.
def add_two_nums(x, y):
    return int(x) + int(y)
total = reduce(add_two_nums, numbers)
print(total)

# 11. Apply reduce to combine the countries list into the sentence shown below.
# Expected output: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
reduced_countries = reduce(lambda x, y: f'{x}, {y}', countries[:-1])
final_sentence = f'{reduced_countries}, and {countries[-1]} are north European countries'
print(final_sentence)

# For exercises 12-15, use the full countries list in data/countries.py.

# 12. Define categorize_countries to return country names matching a shared text pattern, such as 'land', 'ia', 'island', or 'stan'.
def categorize_countries():

# 13. Define a function that counts country names by their first letter and returns a dictionary whose keys are letters and whose values are the counts.


# 14. Define get_first_ten_countries to return the first ten entries from the full countries list, preserving their existing order.


# 15. Define get_last_ten_countries to return the last ten entries from the full countries list, preserving their existing order.


# Exercises: Level 3

# 1. Use the country records in data/countries_data.py to complete all three tasks below.
# a. Create separate sorted lists of the country records: one by name, one by capital, and one by population.
# b. Find the ten languages listed in the most countries, ranked by country count from highest to lowest; count countries, not individual speakers.
# c. Find the ten countries with the largest populations, ranked from highest to lowest.

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


# 6. Use a for loop to print every item in this list:
# ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']


# 7. Loop from 0 through 100 and print only the even numbers.


# 8. Loop from 0 through 100 and print only the odd numbers.


# 1. Loop from 0 through 100, add every number, and print the total.
# Expected total: 5050


# 2. Loop from 0 through 100 and calculate two separate totals:
# one for the even numbers and one for the odd numbers.
# Expected even total: 2550
# Expected odd total: 2500


# 1. Use the countries list from the course's countries.py data file.
# Print every country whose name contains the word "land".


# 2. Reverse this fruit list using a loop:
# ['banana', 'orange', 'mango', 'lemon']


# 3. Use the course's countries_data.py data file to answer these questions:
# - How many unique languages are represented?
# - What are the ten most widely spoken languages?
# - What are the ten most populated countries?

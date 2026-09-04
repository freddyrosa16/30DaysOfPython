import random
import string


# Day 12: Modules

# Exercises: Level 1

# 1. Define random_user_id. Return a random six-character ID made from letters and digits.
# Example output: 1ee33d
def random_user_id():
    number = string.digits
    letters = string.ascii_lowercase
    result = []
    for _ in range(3):
        result.append(random.choice(letters))
        result.append(random.choice(number))
    return ''.join(result)
print(random_user_id())


# 2. Define user_id_gen_by_user. It should take no parameters, but it should ask the user
# for two inputs: the number of characters in each ID and the number of IDs to generate.
# Print each generated ID on a separate line.
def user_id_gen_by_user():
    length = int(input('How long do you want your ID to be?: '))
    quantity = int(input('How many ID"s do you want?: '))

    number = string.digits
    letters = string.ascii_lowercase
    characters = number + letters
    for _ in range(quantity):
        user_id = []
        for _ in range(length):
            user_id.append(random.choice(characters))
        print("".join(user_id))
user_id_gen_by_user()


# 3. Define rgb_color_gen. Return one random RGB color whose red, green, and blue values
# are each between 0 and 255.
# Example output: rgb(125,244,255)
def rgb_color_gen():
    red = random.randint(0 , 255)
    green = random.randint(0, 255)
    blue = random.randint(0 , 255)
    return f'rgb({red},{green},{blue})'
print(rgb_color_gen())

# Exercises: Level 2

# 1. Define list_of_hexa_colors. Accept how many colors the caller wants and return a list
# containing that many random hexadecimal colors. Each color should begin with # and contain
# six characters chosen from 0-9 and a-f.
# Example output: ['#a3e12f', '#03ed55', '#eb3d2b']
def list_of_hexa_colors(amount):
    colors = []
    for _ in range(amount):
        new_color = "#"
        for _ in range(6):
            characters = string.digits + "abcdef"
            new_color += random.choice(characters)
        colors.append(new_color)
    return colors
print(list_of_hexa_colors(4))

# 2. Define list_of_rgb_colors. Accept how many colors the caller wants and return a list
# containing that many random RGB colors.
# Example output: ['rgb(5,55,175)', 'rgb(50,105,100)']
def list_of_rgb_colors(amount):
    colors = []
    for _ in range(amount):
        red = random.randint(0 , 255)
        green = random.randint(0, 255)
        blue = random.randint(0 , 255)
        rgb = f'rgb({red},{green},{blue})'
        colors.append(rgb)
    return colors
print(list_of_rgb_colors(4))

# 3. Define generate_colors. Accept a color type ('hexa' or 'rgb') and an amount.
# Return the requested number of colors in the requested format.
# Example calls:
# generate_colors('hexa', 3)
# generate_colors('rgb', 2)
def generate_colors(color_type, amount):
    if color_type == 'hexa':
        return list_of_hexa_colors(amount)
    elif color_type == 'rgb':
        return list_of_rgb_colors(amount)
    else:
        return 'Pick either the color color type is hexa or rgb'
print(generate_colors('hexa', 4))
print(generate_colors('rgb', 4))

# Exercises: Level 3

# 1. Define shuffle_list. Accept a list and return its items in a random order.
def shuffle_list(lst):
    return sorted(lst, key=lambda x: random.random())
print(shuffle_list([1,2,3,4,5,6,7,8,9]))


# 2. Define a function that returns a list of seven unique random numbers from 0 through 9.
def random_lst():
    st = set()
    while len(st) < 7:
        number = random.randint(0, 9)
        st.add(number)
    return list(st)
print(random_lst())

    # Create an empty tuple.
empty_tuple = tuple()

    # Create separate tuples containing the names of your brothers and sisters. Imaginary siblings are fine.
brothers = ('Jota', 'Rafita', 'Nino', 'Ivan')
sisters = ('Andrea', 'Caludia', 'Yeli')
print(brothers)
print(sisters)

    # Join the brothers and sisters tuples, then assign the result to siblings.
siblings = brothers + sisters
print(siblings)
    # Find how many siblings you have.
print(len(siblings))

    # Add the names of your father and mother to the siblings tuple, then assign the result to family_members.
parents = ('Freddy', 'Maria')
family_members = siblings + parents
print(family_members)

    # Unpack the siblings and parents from family_members.
*siblings, father, mother = family_members
print(siblings)
print(father)
print(mother)

    # Create tuples for fruits, vegetables, and animal products. Join them and assign the result to food_stuff_tp.
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('tomato', 'potato', 'carrot', 'cabbage')
animal_products = ('milk', 'cheese', 'eggs', 'butter')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

    # Convert the food_stuff_tp tuple into a list named food_stuff_lt.
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

    # Slice out the middle item or middle items from food_stuff_tp or food_stuff_lt.
print(food_stuff_tp[5:7])

    # Slice out the first three items and the last three items from food_stuff_lt.
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])

    # Delete the food_stuff_tp tuple completely.
del food_stuff_tp

    # Check whether Estonia and Iceland are Nordic countries using this tuple:
        # nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)

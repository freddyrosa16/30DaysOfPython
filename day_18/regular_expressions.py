from collections import Counter
import re
# Day 18: Regular Expressions
# Source: https://github.com/Asabeneh/30-Days-Of-Python/blob/master/18_Day_Regular_expressions/18_regular_expressions.md

# Exercises: Level 1

# 1. What is the most frequent word in the following paragraph?
paragraph = (
    'I love teaching. If you do not love teaching what else can you love. I '
    'love Python if you do not love something which can give you all the '
    'capabilities to develop an application what else can you love.'
)

# Course example output:
# [
# (6, 'love'),
# (5, 'you'),
# (3, 'can'),
# (2, 'what'),
# (2, 'teaching'),
# (2, 'not'),
# (2, 'else'),
# (2, 'do'),
# (2, 'I'),
# (1, 'which'),
# (1, 'to'),
# (1, 'the'),
# (1, 'something'),
# (1, 'if'),
# (1, 'give'),
# (1, 'develop'),
# (1, 'capabilities'),
# (1, 'application'),
# (1, 'an'),
# (1, 'all'),
# (1, 'Python'),
# (1, 'If')
# ]

# Write your answer below.
word_count = Counter(re.findall(r'\w+', paragraph))
sorted_word_count = sorted(((count, word) for word, count in word_count.items()), reverse=True)
print(sorted_word_count)

# 2. The position of some particles on the horizontal x-axis are -12, -4, -3
# and -1 in the negative direction, 0 at origin, 4 and 8 in the positive
# direction. Extract these numbers from this whole text and find the distance
# between the two furthest particles.
positions = (
    'The position of some particles on the horizontal x-axis are -12, -4, -3 '
    'and -1 in the negative direction, 0 at origin, 4 and 8 in the positive '
    'direction.'
)

# Course example: points = ['-12', '-4', '-3', '-1', '0', '4', '8']
# Expected distance: 20
# Note: the course's sorted_points example includes an extra -1 and 2
# that are not in the input text.

# Write your answer below.


# Exercises: Level 2

# 1. Write a pattern which identifies if a string is a valid python variable

# is_valid_variable('first_name') # True
# is_valid_variable('first-name') # False
# is_valid_variable('1first_name') # False
# is_valid_variable('firstname') # True

# Write your answer below.


# Exercises: Level 3

# 1. Clean the following text. After cleaning, count three most frequent words
# in the string.
sentence = (
    '%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; '
    '&as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found '
    'tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s '
    'mo@tivate yo@u to be a tea@cher!?'
)

# Course example: print(clean_text(sentence))
# I am a teacher and I love teaching There is nothing as more rewarding as
# educating and empowering people I found teaching more interesting than any
# other jobs Does this motivate you to be a teacher
# Course example: print(most_frequent_words(cleaned_text))
# [(3, 'I'), (2, 'teaching'), (2, 'teacher')]

# Write your answer below.

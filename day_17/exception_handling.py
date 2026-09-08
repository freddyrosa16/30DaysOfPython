# Day 17: Exception Handling

# Exercises

# 1. Unpack the list below so that nordic_countries contains the first five
# countries, es contains 'Estonia', and ru contains 'Russia'.
# names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']
names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']
try:
    *nordic_countries, es, ru = names
    print(nordic_countries, es, ru)
except ValueError as e:
    print(e)

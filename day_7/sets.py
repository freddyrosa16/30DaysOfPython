    # Use these collections for the following exercises:
        # it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
        # A = {19, 22, 24, 20, 25, 26}
        # B = {19, 22, 20, 25, 26, 24, 28, 27}
        # age = [22, 19, 24, 25, 26, 24, 25, 24]
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

    # Find the length of it_companies.
print(len(it_companies))

    # Add Twitter to it_companies.
it_companies.add('Twitter')
print(it_companies)

    # Add multiple IT companies to it_companies at once.
ai_companies = {'Nvidia', 'Openai', 'Meta', 'Cursor', 'Xai'}
it_companies.update(ai_companies)
print(it_companies)

    # Remove one company from it_companies.
it_companies.remove('Xai')
print(it_companies)

    # Explain the difference between the remove() and discard() methods.
# We should always check first if the item to be removed is in the set. But if we use remove and the item is not there remove will raise an error, discard does not raise an error.

    # Join sets A and B.
C = A.union(B)
print(C)

    # Find the intersection of A and B.
print(A.intersection(B))

    # Check whether A is a subset of B.
print(A.issubset(B))
print(B.issubset(A))

    # Check whether A and B are disjoint sets.
print(A.isdisjoint(B))

    # Join A with B, then join B with A.
A_with_B = A.union(B)
B_with_A = B.union(A)
print(A_with_B)
print(B_with_A)

    # Find the symmetric difference between A and B.
print(A.symmetric_difference(B))

    # Delete sets A and B completely.
del A
del B

    # Convert age to a set. Compare the length of the original list with the set and determine which is larger.
length_age_lst = len(age)
age_st = set(age)
length_age_st = len(age_st)
print(length_age_lst > length_age_st)

    # Explain the differences between strings, lists, tuples, and sets.
# strings = is one or more characters together surrounded by 1,2, and even threee quote marks. its immutable after creation.
# lists = stores data inside the square brackets, it can be a string, boolean, integer, float. To access them is by index and it starts by 0. Its ordered and is mutable.
# tuples = stores also data types, it is ordered and is immutable.
# sets = stores unique data types, its unordered.

    # Find how many unique words appear in this sentence by using split() and a set:
        # I am a teacher and I love to inspire and teach people.
sentence = 'I am a teacher and I love to inspire and teach people'
words = sentence.split()
words_st = set(words)
unique_words = len(words_st)
print(unique_words)

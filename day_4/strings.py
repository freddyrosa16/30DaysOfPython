    # Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python' and 'Coding', 'For' , 'All' to a single string, 'Coding For All'
print('Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python')
print('Coding' + ' ' + 'For' + ' ' + 'All')

    # Declare a variable named company and assign it to an initial value "Coding For All"
company = 'Coding For All'

    # Print the variable company using print()
print(company)

    # Print the length of the company string using len() method and print()
print(len(company))

    # Change all the characters to uppercase letters using upper() method
print(company.upper())

    # Change all the characters to lowercase letters using lower() method
print(company.lower())

    # Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All
print(company.capitalize())
print(company.title())
print(company.swapcase())

    # Cut(slice) out the first word of Coding For All string
print(company[7:])

    # Check if Coding For All string contains a word Coding using the method index, find or other methods
sub_string = 'Coding'
print(company.find(sub_string))
# If sub_string is missing index produces an error, and find will return -1

    # Replace the word coding in the string 'Coding For All' to Python
print(company.replace('Coding', 'Python'))

    # Change "Python for Everyone" to "Python for All" using the replace method or other methods
python = 'Python For Everyone'
print(python.replace('Everyone', 'All'))

    # Split the string 'Coding For All' using space as the separator (split())
print(company.split())

    # "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma
companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(companies.split(", "))

    # What is the character at index 0 in the string Coding For All
print(company[0]) # at index 0 the character is C

    # What is the last index of the string Coding For All
print(len(company) - 1) # the last index is 13

    # What character is at index 10 in "Coding For All" string
print(company[10]) # the character at index 10 is a space

    # Create an acronym or an abbreviation for the name 'Python For Everyone'
words = python.split()
char1 = words[0][0]
char2 = words[1][0]
char3 = words[2][0]
abbreviation = char1 + char2 + char3
print(abbreviation)

    # Create an acronym or an abbreviation for the name 'Coding For All'
words2 = company.split()
char4 = words2[0][0]
char5 = words2[1][0]
char6 = words2[2][0]
acronym = char4 + char5 + char6
print(acronym)

    # Use index to determine the position of the first occurrence of C in Coding For All
print(company.index('C'))

    # Use index to determine the position of the first occurrence of F in Coding For All
print(company.index('F'))

    # Use rfind to determine the position of the last occurrence of l in Coding For All
print(company.rfind('l'))

    # Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

    # Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))

    # Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence[31 : 54])

    # Does 'Coding For All' start with a substring Coding?
# Yes, this is correct
print(company.startswith('Coding'))

    # Does 'Coding For All' end with a substring coding?
# No, this is false it ends with 'All'
print(company.endswith('coding'))

    # '   Coding For All      '  , remove the left and right trailing spaces in the given string
new_string = '   Coding For All      '
strip_spaces = new_string.strip()
print(strip_spaces)

    # Which one of the following variables return True when we use the method isidentifier():
        # 30DaysOfPython
        # thirty_days_of_python
variable1 = '30DaysOfPython'
variable2 = 'thirty_days_of_python' # This is the variable that return True
print(variable1.isidentifier())
print(variable2.isidentifier())

    # The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string
python_frameworks = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '# '.join(python_frameworks)
print(result)

    # Use the new line escape sequence to separate the following sentences:
        # I am enjoying this challenge.
        # I just wonder what is next.
new_line = 'I am enjoying this challenge\nI just wonder what is next'
print(new_line)

    # Use a tab escape sequence to write the following lines:
        # Name      Age     Country   City
        # Asabeneh  250     Finland   Helsinki
tab1 = 'Name\tAge\tCountry\tCity'
tab2 = 'Asabeneh\t250\tFinland\tHelsinki'
print(tab1.expandtabs(10))
print(tab2.expandtabs(10))

    # Use the string formatting method to display the following:
        # radius = 10
        # area = 3.14 * radius ** 2
        # The area of a circle with radius 10 is 314 meters square.
radius = 10
circle_area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {circle_area:.0f} meters square.')

    # Make the following using string formatting methods:
        # 8 + 6 = 14
        # 8 - 6 = 2
        # 8 * 6 = 48
        # 8 / 6 = 1.33
        # 8 % 6 = 2
        # 8 // 6 = 1
        # 8 ** 6 = 262144
number_one = 8
number_two = 6
addition = number_one + number_two
subtraction = number_one - number_two
multiplication = number_one * number_two
division = number_one / number_two
modulo = number_one % number_two
floor_division = number_one // number_two
exponentiation = number_one ** number_two
print(f'{number_one} + {number_two} = {addition}')
print(f'{number_one} - {number_two} = {subtraction}')
print(f'{number_one} * {number_two} = {multiplication}')
print(f'{number_one} / {number_two} = {division:.2f}')
print(f'{number_one} % {number_two} = {modulo}')
print(f'{number_one} // {number_two} = {floor_division}')
print(f'{number_one} ** {number_two} = {exponentiation}')

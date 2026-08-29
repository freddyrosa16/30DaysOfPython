    # Create an empty list.
lst = list()

    # Create a list containing more than five items.
ai = ['codex', 'claude', 'grok', 'gemini', 'qwen', 'minimax', 'kimi-k', 'deepseek', 'GLM']

    # Find the length of the list.
ai_length = len(ai)

    # Get the first, middle, and last items from the list.
first_item = ai[0]
middle_item = ai[4]
last_item = ai[-1]

    # Create mixed_data_types with your name, age, height, marital status, and address.
mixed_data_types = ['Freddy', 32, "5'8", 'married', 'Puerto Rico']

    # Create it_companies with Facebook, Google, Microsoft, Apple, IBM, Oracle, and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

    # Print the companies list.
print(it_companies)

    # Print the number of companies.
print(len(it_companies))

    # Print the first, middle, and last companies.
print(it_companies[0], it_companies[3], it_companies[-1])

    # Modify one company, then print the updated list.
it_companies[0] = 'Meta'
print(it_companies)
    # Add another IT company to the end of the list.
it_companies.append('Netflix')
print(it_companies)

    # Insert an IT company in the middle of the list.
it_companies.insert(3, 'Nvidia')
print(it_companies)

    # Change one company name to uppercase, excluding IBM.
it_companies[3] = 'NVIDIA'
print(it_companies)

    # Join the company names using the string '#;  '.
joined_it_companies = ('#;  ').join(it_companies)
print(joined_it_companies)

    # Check whether a chosen company exists in the list.
print('Netflix' in it_companies)

    # Sort the companies using the sort() method.
it_companies.sort()
print(it_companies)

    # Reverse the list so the companies appear in descending order.
it_companies.reverse()
print(it_companies)

    # Slice out the first three companies.
print(it_companies[:3])

    # Slice out the last three companies.
print(it_companies[6:])

    # Slice out the middle company, or the two middle companies when needed.
print(it_companies[4:5])

    # Remove the first company from the list.
it_companies.remove('Oracle')
print(it_companies)

    # Remove the middle company, or middle companies, from the list.
it_companies.remove('Meta')
it_companies.remove('IBM')
print(it_companies)

    # Remove the last company from the list.
it_companies.remove('Amazon')
print(it_companies)

    # Remove every item from the companies list.
it_companies.clear()
print(it_companies)

    # Delete the companies list completely.
del it_companies

    # Join these two lists:
        # front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
        # back_end = ['Node', 'Express', 'MongoDB']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full = front_end + back_end

    # Copy the joined list into full_stack, then place Python and SQL after Redux.
full_stack = full.copy()
print(full_stack.index('Redux')) # index 4
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

    # Use this list of student ages:
        # ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
        # Sort the ages and find the minimum and maximum.
        # Add the minimum and maximum ages to the list again.
        # Calculate the median age.
        # Calculate the average age.
        # Calculate the age range: maximum minus minimum.
        # Compare abs(minimum - average) with abs(maximum - average).
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
minimum = ages[0]
maximum = ages[-1]
ages.append(19)
ages.append(26)

sorted_ages = sorted(ages)
n = len(sorted_ages)
mid = n // 2
left = sorted_ages[:mid]
right = sorted_ages[mid:]
median = (left[-1] + right[0]) / 2
print(median)

total = sum(sorted_ages)
average = total / n
print(average)

age_range = maximum - minimum
print(age_range)

abs1 = abs(minimum - average)
abs2 = abs(maximum - average)
print(abs1 != abs2)

    # Find the middle country or countries in the countries list.
countries = [
    'Afghanistan',
    'Albania',
    'Algeria',
    'Andorra',
    'Angola',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bhutan',
    'Bolivia',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cabo Verde',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Colombia',
    'Comoros',
    'Congo, Democratic Republic of the',
    'Congo, Republic of the',
    'Costa Rica',
    "Côte d'Ivoire",
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'East Timor (Timor-Leste)',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Eswatini',
    'Ethiopia',
    'Fiji',
    'Finland',
    'France',
    'Gabon',
    'Gambia',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Grenada',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Korea, North',
    'Korea, South',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Mauritania',
    'Mauritius',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Montenegro',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'North Macedonia',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Palestine',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Qatar',
    'Romania',
    'Russia',
    'Rwanda',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Vincent and the Grenadines',
    'Samoa',
    'San Marino',
    'Sao Tome and Principe',
    'Saudi Arabia',
    'Senegal',
    'Serbia',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'South Sudan',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Sweden',
    'Switzerland',
    'Syria',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Togo',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United States',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
    'Yemen',
    'Zambia',
    'Zimbabwe'
]

countries_length = len(countries)
mid = countries_length // 2
print(countries[mid])

    # Split the countries into two halves; when odd, put one extra country in the first half.
left = countries[:mid + 1]
print(left)
print(len(left))
right = countries[mid + 1:]
print(right)
print(len(right))

    # Unpack China, Russia, and USA separately, and collect the remaining countries as scandic countries:
        # ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
new_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia, usa, *scandic_countries = new_countries

print(china)
print(russia)
print(usa)
print(scandic_countries)

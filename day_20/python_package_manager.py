import requests
import json
import statistics


# 1. Fetch Romeo and Juliet from the URL below and report its 10 most
# frequent words.
# URL: https://www.gutenberg.org/ebooks/1112.txt.utf-8
# This is an updated link for the course's Gutenberg ebook 1112.

# Write your answer below.
def most_frequent_words():
    word_dict = {}
    url = "https://www.gutenberg.org/ebooks/1112.txt.utf-8"
    response = requests.get(url)
    response.raise_for_status()
    text = response.text
    splitted_text = text.split()
    for word in splitted_text:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    sorted_words = sorted(((count, word) for word, count in word_dict.items()), reverse=True)
    return sorted_words[:10]
print(most_frequent_words())

# 2. Fetch the cat breeds and complete these summaries:
# URL: https://api.thecatapi.com/v1/breeds
# a. Minimum, maximum, mean, median, and standard deviation of weight (kg).
# b. The same five statistics for lifespan (years).
# c. A frequency table showing countries and their cat breeds.
# Clarification: weight and lifespan can be ranges. State how you turn
# each range into a number, and whether your standard deviation describes
# the population or a sample. The course does not specify these choices.

# Write your answer below.
def dog_api():
    # cat api does not work search for a dog one that does
    weight_list = []
    url = "https://dogapi.dog/api/v2/breeds"
    response = requests.get(url)
    response.raise_for_status()
    breeds = response.json()["data"]
    for breed in breeds:
        attributes = breed["attributes"]
        male_weight = (attributes['male_weight']['min'] + attributes['male_weight']['max']) / 2
        female_weight = (attributes['female_weight']['min'] + attributes['female_weight']['max']) / 2
        weight = (male_weight + female_weight) / 2
        weight_list.append(weight)
    # min, max
    min_weight = min(weight_list)
    max_weight = max(weight_list)

    # mean
    mean_weight = statistics.mean(weight_list)

    # median
    median_weight = statistics.median(weight_list)

    # standard deviation
    standard_deviation = statistics.pstdev(weight_list)
print(cat_breed())


print(cat_breed())

# 3. Fetch country records and determine:
# a. The 10 largest countries by area.
# b. The 10 languages listed by the most countries.
# c. The number of distinct languages across all countries.
# Course URL: https://restcountries.eu/rest/v2/all
# Alternative endpoint to try:
# https://restcountries.com/v3.1/all?fields=name,area,languages
# The alternative uses a different JSON structure; inspect it first.

# Write your answer below.


# 4. Retrieve and inspect the UCI dataset listing using BeautifulSoup4.
# URL: https://archive.ics.uci.edu/datasets
# This replaces the course's older /ml/datasets.php link.

# Write your answer below.


# Setup notes:
# requests and beautifulsoup4 are third-party packages for this lesson.
# Use your Python environment's pip to install them before importing them.
# Source check: September 13, 2026. The cat and alternative country APIs
# returned HTTP 403 during setup here; their data could not be verified.
# Check response status before reading JSON. An access error does not
# necessarily mean your Python code is wrong.

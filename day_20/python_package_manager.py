import requests
import json
import statistics
from bs4 import BeautifulSoup

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
    sorted_words = sorted(
        ((count, word) for word, count in word_dict.items()), reverse=True
    )
    return sorted_words[:10]


print(most_frequent_words(), "\n")

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
    life_span_list = []
    frequency_list = []
    url = "https://dogapi.dog/api/v2/breeds"
    response = requests.get(url)
    response.raise_for_status()
    breeds = response.json()["data"]
    country_breeds = {}
    for breed in breeds:
        attributes = breed["attributes"]
        origin = attributes["origin"]
        if "country" in origin:
            country = origin["country"]
        else:
            country = "Unknown"
        name = attributes["name"]
        male_weight = (
            attributes["male_weight"]["min"] + attributes["male_weight"]["max"]
        ) / 2
        female_weight = (
            attributes["female_weight"]["min"] + attributes["female_weight"]["max"]
        ) / 2
        weight = (male_weight + female_weight) / 2
        weight_list.append(weight)

        # lifespan
        lifespan = (attributes["life"]["min"] + attributes["life"]["max"]) / 2
        life_span_list.append(lifespan)

        # Frequency
        if country not in country_breeds:
            country_breeds[country] = []
        country_breeds[country].append(name)

    # weight
    # min, max
    min_weight = min(weight_list)
    max_weight = max(weight_list)

    # mean
    mean_weight = statistics.mean(weight_list)

    # median
    median_weight = statistics.median(weight_list)

    # standard deviation
    standard_deviation_weight = statistics.pstdev(weight_list)

    # lifespan
    # min, max
    min_lifespan = min(life_span_list)
    max_lifespan = max(life_span_list)

    # mean
    mean_lifespan = statistics.mean(life_span_list)

    # median
    median_lifespan = statistics.median(life_span_list)

    # standard deviation
    standard_deviation_lifespan = statistics.pstdev(life_span_list)

    # Frequency
    for country, names in country_breeds.items():
        frequency_list.append((country, len(names), names))

    return {
        "weight": {
            "min": min_weight,
            "max": max_weight,
            "mean": mean_weight,
            "median": median_weight,
            "std_deviation": standard_deviation_weight,
        },
        "lifespan": {
            "min": min_lifespan,
            "max": max_lifespan,
            "mean": mean_lifespan,
            "median_lifespan": median_lifespan,
            "std_deviation": standard_deviation_lifespan,
        },
        "frequency": {
            country: {"count": len(names), "breeds": names}
            for country, names in country_breeds.items()
        },
    }


print(dog_api(), "\n")

# 3. Fetch country records and determine:
# a. The 10 largest countries by area.
# b. The 10 languages listed by the most countries.
# c. The number of distinct languages across all countries.
# Course URL: https://restcountries.eu/rest/v2/all
# Alternative endpoint to try:
# https://restcountries.com/v3.1/all?fields=name,area,languages
# The alternative uses a different JSON structure; inspect it first.


# Write your answer below.
def country_record_area():
    url = "https://raw.githubusercontent.com/mledoze/countries/master/countries.json"
    response = requests.get(url)
    response.raise_for_status()
    country_info = response.json()
    country_area = {}
    for country in country_info:
        name = country['name']['official']
        country_area[name] = country['area']
    sorted_countries_area = sorted(((area, country) for country, area in country_area.items()), reverse=True, key=lambda x: x[0])
    return sorted_countries_area[:10]
print(country_record_area(), '\n')

def country_records_language():
    url = "https://raw.githubusercontent.com/mledoze/countries/master/countries.json"
    response = requests.get(url)
    response.raise_for_status()
    country_info = response.json()
    country_language = {}
    for country in country_info:
        languages = country['languages'].values()
        for language in languages:
            if language not in country_language:
                country_language[language] = 1
            else:
                country_language[language] += 1
    sorted_language = sorted(((count, country) for country, count in country_language.items()), reverse=True, key=lambda x: x[0])
    return sorted_language[:10]
print(country_records_language(), '\n')

def distinct_languages():
    url = "https://raw.githubusercontent.com/mledoze/countries/master/countries.json"
    response = requests.get(url)
    response.raise_for_status()
    country_info = response.json()
    language_set = set()
    for country in country_info:
        languages = country['languages'].values()
        for language in languages:
            language_set.add(language)
    return f'The number of distinct langugages is {len(language_set)}, and the langugages are: {language_set}'
print(distinct_languages(), '\n')


# 4. Retrieve and inspect the UCI dataset listing using BeautifulSoup4.
# URL: https://archive.ics.uci.edu/datasets
# This replaces the course's older /ml/datasets.php link.

# Write your answer below.
def uci_dataset():
    url = "https://archive.ics.uci.edu/datasets"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.title
print(uci_dataset())

# Setup notes:
# requests and beautifulsoup4 are third-party packages for this lesson.
# Use your Python environment's pip to install them before importing them.
# Source check: September 13, 2026. The cat and alternative country APIs
# returned HTTP 403 during setup here; their data could not be verified.
# Check response status before reading JSON. An access error does not
# necessarily mean your Python code is wrong.

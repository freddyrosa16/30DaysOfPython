# Exercises: Level 1
import json
import os
import re

# 1. Create a function that reports line and word totals for each speech:
# data/obama_speech.txt
# data/michelle_obama_speech.txt
# data/donald_speech.txt
# data/melina_trump_speech.txt

# Write your answer below.
def speech(txt):
    word_total = 0
    with open(txt) as f:
        lines = f.read().splitlines()
        for line in lines:
            word_total += len(line.split())
    name = txt.split('/')[-1].split('.')[0]
    return f'{name} has {len(lines)} lines and {word_total} words'
print(speech('data/obama_speech.txt'),'\n')
print(speech("data/michelle_obama_speech.txt"),'\n')
print(speech("data/donald_speech.txt"),'\n')
print(speech("data/melina_trump_speech.txt"),'\n')


# 2. Using data/countries_data.json, rank languages by how many countries
# list them. Return the top 10, then try 3.
# Function: most_spoken_languages(filename, n)
# Return format: [(country_count, language), ...]

# Write your answer below.
def most_spoken_languages(filename, n):
    language_count = {}
    with open(filename) as f:
        countries = json.load(f)
        for country in countries:
            for language in country["languages"]:
                if language not in language_count:
                    language_count[language] = 1
                else:
                    language_count[language] += 1
    ranked_languages = sorted(((count, lang) for lang, count in language_count.items()), reverse=True, key=lambda x: x[0])
    return ranked_languages[:n]
print(most_spoken_languages("data/countries_data.json", 10))
print(most_spoken_languages("data/countries_data.json", 3))

# 3. Rank countries in that JSON by population. Return 10, then 3.
# Function: most_populated_countries(filename, n)
# Return format: [{'country': name, 'population': population}, ...]

# Write your answer below.
def most_populated_countries(filename, n):
    population_list = []
    with open(filename) as f:
        countries = json.load(f)
        for country in countries:
            countries_pop_dict = {
                'country': country['name'],
                'population': country['population']
            }
            population_list.append(countries_pop_dict)
    sorted_population = sorted(population_list, reverse=True, key=lambda x: x['population'])
    return sorted_population[:n]
print(most_populated_countries("data/countries_data.json", 10))
print(most_populated_countries("data/countries_data.json", 3))


# Exercises: Level 2

# 1. Collect incoming senders' email addresses from
# data/email_exchanges_big.txt into a list.

# Write your answer below.
def sender_email(txt):
    emails = []
    with open(txt) as f:
        for lines in f:
            if lines.startswith("From:"):
                splitted = lines.split()
                emails.append(splitted[1])
    return emails
print(sender_email("data/email_exchanges_big.txt"))

# 2. Implement find_most_common_words(text_or_file, n), returning
# (count, word) tuples ordered by decreasing frequency. Try n=10 and n=5.

# Write your answer below.
def find_most_common_words(text_or_file, n):
    word_dict = {}
    if os.path.exists(text_or_file):
        with open(text_or_file) as f:
            for lines in f:
                splitted_lines = lines.split()
                for word in splitted_lines:
                    if word not in word_dict:
                        word_dict[word] = 1
                    else:
                        word_dict[word] += 1
        sorted_words = sorted(((count, word) for word, count in word_dict.items()), reverse=True)
        return sorted_words[:n]
    else:
        splitted_lines = text_or_file.split()
        for word in splitted_lines:
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1
        sorted_words = sorted(((count, word) for word, count in word_dict.items()), reverse=True)
        return sorted_words[:n]
print(find_most_common_words("data/email_exchanges_big.txt", 10))
print(find_most_common_words("data/email_exchanges_big.txt", 5))

# 3. Reuse that function to report each speech's 10 most frequent words.

# Write your answer below.
print(find_most_common_words("data/obama_speech.txt", 10))
print(find_most_common_words("data/michelle_obama_speech.txt", 10))
print(find_most_common_words("data/donald_speech.txt", 10))
print(find_most_common_words("data/melina_trump_speech.txt", 10))


# 4. Compare Michelle's and Melina's speeches for similarity. Accept text
# or files; use clean_text, remove_support_words, and check_text_similarity.
# Stop words: data/stop_words.py

# Write your answer below.
def clean_text(txt):
    clean_text = re.sub(r"[^\w\s]", "", txt).lower()
    return clean_text

# 5. Report the top 10 words in data/romeo_and_juliet.txt.

# Write your answer below.


# 6. In data/hacker_news.csv, count lines containing:
# a. python or Python
# b. JavaScript, javascript, or Javascript
# c. Java, excluding JavaScript

# Write your answer below.

# additional_calculations.py
import math

def calculate_hartley_entropy(alphabet_size):
    entropy = math.log2(alphabet_size)
    return entropy

def calculate_shannon_entropy(text):
    total_characters = len(text)
    char_counts = {}

    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    entropy = 0
    for count in char_counts.values():
        probability = count / total_characters
        entropy -= probability * math.log2(probability)

    return entropy

def calculate_alphabet_redundancy(alphabet_size, message_length):
    redundancy = 1 - (1 / alphabet_size)
    return redundancy
def calculate_entropy(data):
    total_count = len(data)
    if total_count == 0:
        return 0

    value_counts = {}
    for value in data:
        if value in value_counts:
            value_counts[value] += 1
        else:
            value_counts[value] = 1

    entropy = 0
    for count in value_counts.values():
        probability = count / total_count
        entropy -= probability * math.log2(probability)

    return entropy

def calculate_alphabet_size(text):
    unique_characters = set(text.lower())
    alphabet_size = len(unique_characters)
    return alphabet_size


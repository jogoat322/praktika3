import math

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

def save_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# Пример использования
choice = input("Выберите действие (1 - расчет мощности алфавита, 2 - расчет энтропии, 3 - дополнительные расчеты): ")

if choice == '1':
    text = input("Введите текст для анализа: ")
    alphabet_size = calculate_alphabet_size(text)
    print(f"Мощность алфавита: {alphabet_size}")
    filename = input("Введите имя файла для сохранения результата: ")
    save_to_file(filename, f"Мощность алфавита: {alphabet_size}")

elif choice == '2':
    data = [int(x) for x in input("Введите данные через пробел (например, 1 1 1 0 0 1 0 1 0 0): ").split()]
    entropy_value = calculate_entropy(data)
    print(f"Энтропия данных: {entropy_value}")
    filename = input("Введите имя файла для сохранения результата: ")
    save_to_file(filename, f"Энтропия данных: {entropy_value}")

elif choice == '3':
    text = input("Введите текст для дополнительных расчетов: ")
    alphabet_size = calculate_alphabet_size(text)
    hartley_entropy = calculate_hartley_entropy(alphabet_size)
    shannon_entropy = calculate_shannon_entropy(text)
    message_length = len(text)
    alphabet_redundancy = calculate_alphabet_redundancy(alphabet_size, message_length)

    print(f"Мощность алфавита: {alphabet_size}")
    print(f"Информационная энтропия по Хартли: {hartley_entropy}")
    print(f"Информационная энтропия по Шеннону: {shannon_entropy}")
    print(f"Избыточность алфавита для кодирования сообщения: {alphabet_redundancy}")

    filename = input("Введите имя файла для сохранения результата: ")
    content = f"Мощность алфавита: {alphabet_size}\nИнформационная энтропия по Хартли: {hartley_entropy}\nИнформационная энтропия по Шеннону: {shannon_entropy}\nИзбыточность алфавита для кодирования сообщения: {alphabet_redundancy}"
    save_to_file(filename, content)

else:
    print("Неверный выбор действия. Пожалуйста, выберите 1, 2 или 3.")

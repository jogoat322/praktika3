import math

def calculate_entropy(data):
    """
    Рассчитывает энтропию для переданных данных.

    Параметры:
    - data: список значений (например, список классов в случае задачи классификации)

    Возвращает:
    - entropy: значение энтропии
    """
    total_count = len(data)
    if total_count == 0:
        return 0  # Если данных нет, энтропия равна 0

    # Подсчет количества каждого уникального значения
    value_counts = {}
    for value in data:
        if value in value_counts:
            value_counts[value] += 1
        else:
            value_counts[value] = 1

    # Расчет энтропии
    entropy = 0
    for count in value_counts.values():
        probability = count / total_count
        entropy -= probability * math.log2(probability)

    return entropy

def calculate_alphabet_size(text):
    """
    Определяет мощность алфавита для переданного текста.

    Параметры:
    - text: текст для анализа

    Возвращает:
    - alphabet_size: мощность алфавита
    """
    unique_characters = set(text.lower())
    alphabet_size = len(unique_characters)
    return alphabet_size

# Пример использования
text = "Я помню чудное мгновенье"
alphabet_size = calculate_alphabet_size(text)
print(f"Мощность алфавита: {alphabet_size}")

data = [1, 1, 1, 0, 0, 1, 0, 1, 0, 0]
entropy_value = calculate_entropy(data)
print(f"Энтропия данных: {entropy_value}")

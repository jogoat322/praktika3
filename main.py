# main.py
from additional_calculations import (
    calculate_hartley_entropy,
    calculate_shannon_entropy,
    calculate_alphabet_redundancy,
    calculate_entropy,
    calculate_alphabet_size

)

def save_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

while True:
    choice = input("Выберите действие (1 - расчет мощности алфавита, 2 - расчет энтропии, 3 - дополнительные расчеты, 0 - выход): ")

    if choice == '0':
        print("До свидания!")
        break

    if choice == '1':
        text = input("Введите текст для анализа: ")
        alphabet_size = calculate_alphabet_size(text)
        print(f"Мощность алфавита: {alphabet_size}")
        save_choice = input("Хотите ли сохранить результат в файл? (y/n): ")
        if save_choice.lower() == 'y':
            filename = input("Введите имя файла для сохранения результата: ")
            save_to_file(filename, f"Мощность алфавита: {alphabet_size}")

    elif choice == '2':
        data = [int(x) for x in input("Введите данные через пробел (например, 1 1 1 0 0 1 0 1 0 0): ").split()]
        entropy_value = calculate_data_entropy(data)
        print(f"Энтропия данных: {entropy_value}")
        save_choice = input("Хотите ли сохранить результат в файл? (y/n): ")
        if save_choice.lower() == 'y':
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

        save_choice = input("Хотите ли сохранить результат в файл? (y/n): ")
        if save_choice.lower() == 'y':
            filename = input("Введите имя файла для сохранения результата: ")
            content = f"Мощность алфавита: {alphabet_size}\nИнформационная энтропия по Хартли: {hartley_entropy}\nИнформационная энтропия по Шеннону: {shannon_entropy}\nИзбыточность алфавита для кодирования сообщения: {alphabet_redundancy}"
            save_to_file(filename, content)

    else:
        print("Неверный выбор действия. Пожалуйста, выберите 1, 2, 3 или 0 для выхода.")
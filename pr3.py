import math

def calculate_entropy(probabilities):
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
    return entropy

def main():
    # Пример: вероятности символов в сообщении
    # Замените эти значения своими данными
    probabilities = [0.2, 0.1, 0.4, 0.3]

    # Расчет энтропии
    entropy = calculate_entropy(probabilities)

    # Вывод результата
    print(f"Вероятности символов: {probabilities}")
    print(f"Энтропия источника сообщений: {entropy:.4f} бит")

if __name__ == "__main__":
    main()

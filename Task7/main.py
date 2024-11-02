import random
import matplotlib.pyplot as plt


def monte_carlo_simulation(num_rolls):
    # Ініціалізація лічильника для кожної суми від 2 до 12
    counts = {i: 0 for i in range(2, 13)}

    # Симуляція кидків кубиків
    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        counts[total] += 1

    # Обчислення ймовірностей для кожної суми
    probabilities = {total: count / num_rolls * 100 for total, count in counts.items()}
    return probabilities


def plot_results(simulated_probabilities, theoretical_probabilities):
    sums = list(simulated_probabilities.keys())
    simulated_values = list(simulated_probabilities.values())
    theoretical_values = [theoretical_probabilities[s] for s in sums]

    # Побудова графіка
    plt.figure(figsize=(10, 6))
    plt.bar(sums, simulated_values, color='skyblue', label='Монте-Карло')
    plt.plot(sums, theoretical_values, color='red', marker='o', linestyle='-', label='Теоретична ймовірність')
    plt.xlabel('Сума')
    plt.ylabel('Ймовірність (%)')
    plt.title('Ймовірність сум при киданні двох кубиків')
    plt.legend()
    plt.show()


def main():
    # Теоретичні ймовірності для кожної суми від 2 до 12
    theoretical_probabilities = {
        2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11,
        6: 13.89, 7: 16.67, 8: 13.89, 9: 11.11,
        10: 8.33, 11: 5.56, 12: 2.78
    }

    # Виконуємо симуляцію
    num_rolls = 100000  # Кількість кидків
    simulated_probabilities = monte_carlo_simulation(num_rolls)

    # Виводимо ймовірності
    print("Результати симуляції методом Монте-Карло:")
    for total, prob in simulated_probabilities.items():
        print(f"Сума {total}: {prob:.2f}%")

    # Порівнюємо з теоретичними значеннями
    print("\nТеоретичні ймовірності:")
    for total, prob in theoretical_probabilities.items():
        print(f"Сума {total}: {prob:.2f}%")

    # Побудова графіка для порівняння
    plot_results(simulated_probabilities, theoretical_probabilities)


if __name__ == "__main__":
    main()

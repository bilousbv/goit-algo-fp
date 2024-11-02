def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням калорій до вартості в спадному порядку
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)

    total_calories = 0
    selected_items = []
    current_budget = budget

    for item, info in sorted_items:
        if info["cost"] <= current_budget:
            selected_items.append(item)
            total_calories += info["calories"]
            current_budget -= info["cost"]

    return selected_items, total_calories


def dynamic_programming(items, budget):
    # Ініціалізуємо таблицю DP, де dp[b] — максимальна калорійність для бюджету b
    dp = [0] * (budget + 1)
    item_selection = [[] for _ in range(budget + 1)]

    for item, info in items.items():
        cost = info["cost"]
        calories = info["calories"]

        for b in range(budget, cost - 1, -1):
            if dp[b - cost] + calories > dp[b]:
                dp[b] = dp[b - cost] + calories
                item_selection[b] = item_selection[b - cost] + [item]

    return item_selection[budget], dp[budget]


def main():
    # Приклад використання
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    budget = 100
    selected_items_greedy, total_calories_greedy = greedy_algorithm(items, budget)
    selected_items_dp, total_calories_dp = dynamic_programming(items, budget)

    print("Жадібний алгоритм:")
    print(f"Обрані страви: {selected_items_greedy}")
    print(f"Загальна калорійність: {total_calories_greedy}")

    print("\nАлгоритм динамічного програмування:")
    print(f"Обрані страви: {selected_items_dp}")
    print(f"Загальна калорійність: {total_calories_dp}")


if __name__ == "__main__":
    main()

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(budget: int):
    result = []
    calories = 0
    b = budget

    items_with_ratio = sorted([
        {'name': key, 'ratio': value['calories'] / value['cost'], 'cost': value['cost'], 'calories': value['calories']} for key, value in items.items()], key=lambda d: d['ratio'], reverse=True)

    possible_items = [item for item in items_with_ratio if item['cost'] <= b]

    for item in possible_items:
        b -= item['cost']

        if b < 0:
            break

        calories += item['calories']
        result.append(item['name'])

        if b <= 0:
            break

    return result, calories


def dynamic_programming(budget: int):
    item_list = list(items.items())
    n = len(item_list)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, info = item_list[i - 1]
        cost = info["cost"]
        calories = info["calories"]

        for b in range(budget + 1):
            if cost <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + calories)
            else:
                dp[i][b] = dp[i - 1][b]

    result = []
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            name, info = item_list[i - 1]
            result.append(name)
            b -= info["cost"]

    result.reverse()
    return result, dp[n][budget]

print(greedy_algorithm(100))
print(dynamic_programming(100))
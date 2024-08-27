def min_cost_to_level_hills(hills):
    hills.sort()
    n = len(hills)
    min_cost = float('inf')

    for lower in range(min(hills), max(hills) - 16):
        upper = lower + 17
        cost = 0
        for h in hills:
            if h < lower:
                cost += (lower - h) ** 2
            elif h > upper:
                cost += (h - upper) ** 2
        min_cost = min(min_cost, cost)

    return min_cost


N = int(input())
hills = [int(input()) for _ in range(N)]

result = min_cost_to_level_hills(hills)
print(result)
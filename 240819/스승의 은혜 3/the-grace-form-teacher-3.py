N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]

# Sort gifts by total cost
gifts.sort(key=lambda x: x[0] + x[1])

max_count = 0
for i in range(N):
    budget = B
    count = 0

    for j, (price, shipping) in enumerate(gifts):
        current_cost = price + shipping
        if j == i:
            current_cost = price // 2 + shipping

        if budget >= current_cost:
            budget -= current_cost
            count += 1

    max_count = max(max_count, count)

print(max_count)
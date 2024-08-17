N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]

# Filter out gifts with odd prices
gifts = [gift for gift in gifts if gift[0] % 2 == 0]

# Sort gifts by total cost
gifts.sort(key=lambda x: x[0] + x[1])

max_count = 0

for i in range(len(gifts)):
    budget = B
    count = 0
    
    for j, (price, shipping) in enumerate(gifts):
        current_cost = price + shipping
        if j == i:
            current_cost = price // 2 + shipping
        
        if budget >= current_cost:
            budget -= current_cost
            count += 1
        else:
            break
    
    max_count = max(max_count, count)

print(max_count)
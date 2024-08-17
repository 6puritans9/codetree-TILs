N, B = map(int, input().split())
# price P(i); shipping S(i) per student
table = [tuple(map(int, input().split()))for _ in range(N)]

for i in range(N):
    for j in range(N - i - 1):
        if table[j] > table[j+1]:
            table[j], table[j+1] = table[j+1], table[j]

max_count = 0
for i in range(N):
    budget = B
    count = 0
    
    for j in range(N):
        price, shipping = table[j][0], table[j][1]
        current_cost = price + shipping

        if i == j and not budget < (price // 2 + shipping):
            discounted = price // 2
            current_cost = discounted + shipping
            
            budget -= current_cost
            count += 1
            continue

        if budget < current_cost:
            break      
        
        budget -= (price + shipping)
        count += 1

    max_count = max(max_count, count)

print(max_count)
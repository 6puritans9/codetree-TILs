N, B = map(int, input().split())
# price P(i); shipping S(i) per student
table = [tuple(map(int, input().split()))for _ in range(N)]

# for i in range(N):
#     for j in range(N - i - 1):
#         if sum(table[j]) > sum(table[j+1]):
#             table[j], table[j+1] = table[j+1], table[j]

table.sort(key=lambda x: x[0] + x[1])

max_count = 0
for i in range(N):
    budget = B
    count = 0
    
    for j in range(N):
        price, shipping = table[j]
        
        if i == j:
            current_cost = (price // 2) + shipping
        else:
            current_cost = price + shipping

        if budget < current_cost:
            break
        else:
            budget -= current_cost
            count += 1

    max_count = max(max_count, count)

print(max_count)
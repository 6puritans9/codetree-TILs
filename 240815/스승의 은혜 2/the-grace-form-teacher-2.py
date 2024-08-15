N, B = tuple(map(int, input().split()))
prices = [int(input()) for _ in range(N)]
prices. sort()

max_count = 0
for i in range(N):    
    budget = B
    present_count = 0
    discounted = prices[i] // 2
    
    for j in range(N):
        if budget >= discounted and i == j:
            budget -= discounted
            present_count += 1
            continue
        
        if budget >= prices[j]:
            budget -= prices[j]
            present_count += 1
            continue

        break
    
    max_count = max(max_count, present_count)

print(max_count)
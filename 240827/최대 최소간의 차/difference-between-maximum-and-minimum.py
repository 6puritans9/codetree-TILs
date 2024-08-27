n, k = map(int, input().split())
numbers = list(map(int, input().split()))

min_num, max_num = min(numbers), max(numbers)
answer = float("inf")
for lower in range(min_num, max_num + 1):
    upper = lower + k
    total_cost = 0

    for num in numbers:
        cost = 0
        if num < lower:
            cost = lower - num
        elif num > upper:
            cost = num - upper
        
        total_cost += cost

    answer = min(answer, total_cost)

print(answer)
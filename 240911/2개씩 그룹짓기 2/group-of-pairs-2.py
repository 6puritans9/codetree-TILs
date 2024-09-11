n = int(input())
numbers = list(map(int, input().split()))
length = n*2

max_min = -1
for i in range(length):
    min_diff = float("inf")
    
    for j in range(length):
        if i == j:
            continue
        
        min_diff = min(min_diff, abs(numbers[i] - numbers[j]))
    
    max_min = max(max_min, min_diff)

print(max_min)
n = int(input())
numbers = list(map(int, input().split()))

max_sum = 0
for i in range(n-2):
    for j in range(i+2, n):
        sum = numbers[i] + numbers[j]
    
        if sum > max_sum:
            max_sum = sum

print(max_sum)
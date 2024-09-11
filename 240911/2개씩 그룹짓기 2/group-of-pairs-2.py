n = int(input())
numbers = list(map(int, input().split()))
length = n*2

max_min = 0
numbers.sort()
for i in range(1, length, 2):
    diff = numbers[i] - numbers[i-1]

    max_min = max(max_min, diff)

print(max_min)
n = int(input())
numbers = list(map(int, input().split()))
max_number = max(numbers)

max_count = 0
for k in range(1, max_number + 1):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            num1 = numbers[i]
            num2 = numbers[j]

            if abs(num1 - k) == abs(num2 - k):
                count += 1

        max_count = max(max_count, count)

print(max_count)
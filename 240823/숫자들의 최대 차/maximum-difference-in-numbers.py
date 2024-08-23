N, K = map(int, input().split())
numbers = [int(input()) for _ in range(N)]

max_count = 0
for i in range(N - 1):
    number1 = numbers[i]
    count = 0

    for j in range(N - 1):
        number2 = numbers[j]

        if abs(number1 - number2) <= K:
            count += 1

    max_count = max(max_count, count)

print(max_count)
N, K = map(int, input().split())
numbers = [int(input()) for _ in range(N)]
numbers.sort()

max_count = 0
start = 0

for end in range(N):
    while numbers[end] - numbers[start] > K:
        start += 1
    max_count = max(max_count, end - start + 1)

print(max_count)
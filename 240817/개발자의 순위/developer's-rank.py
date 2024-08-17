K, N = tuple(map(int, input().split()))
inputs = [tuple(map(int, input().split())) for _ in range(K)]

array = [[0 for _ in range(N+1)] for _ in range(N+1)]

for input in inputs:
    for i in range(N-1):
        for j in range(i+1, N):
            row, col = input[i], input[j]

            array[row][col] += 1

count = 0
for row in array:
    for col in row:
        if col == K:
            count += 1

print(count)
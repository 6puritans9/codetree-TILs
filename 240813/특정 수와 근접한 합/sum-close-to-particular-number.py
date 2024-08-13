N, S = tuple(map(int, input().split()))
numbers = list(map(int, input().split()))
total_sum = sum(numbers)

min_diff = float("inf")
for i in range(N-1):
    for j in range(i+1, N):
        exclusion_sum = numbers[i] + numbers[j]
        temp_sum = total_sum - exclusion_sum

        min_diff = min(min_diff, abs(S - temp_sum))

print(min_diff)
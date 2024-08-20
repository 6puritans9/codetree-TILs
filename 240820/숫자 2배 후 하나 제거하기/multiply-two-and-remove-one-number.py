n = int(input())
numbers = list(map(int, input().split()))

min_diff = float("inf")
for i, outer_number in enumerate(numbers):
    numbers[i] *= 2

    for j in range(n):
        sub_numbers = [inner_number for k, inner_number in enumerate(numbers) if k != j]

        diff = 0
        for k in range(len(sub_numbers) - 1):
            diff += abs(sub_numbers[k] - sub_numbers[k + 1])

        min_diff = min(min_diff, diff)

    numbers[i] //= 2

print(min_diff)
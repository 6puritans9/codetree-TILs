def get_candidate(numbers, i, j):
    return sum(numbers) - (numbers[i] + numbers[j])

def get_closest_diff(target, numbers, length):
    difference = float("inf")

    for i in range(length-1):
        for j in range(i+1, length):
            candidate = get_candidate(numbers, i, j)
            difference = min(difference, abs(target - candidate))

    return difference


N, S = list(map(int, input().split()))
numbers = list(map(int, input().split()))

print(get_closest_diff(S, numbers, N))
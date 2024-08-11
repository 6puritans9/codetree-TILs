def get_candidate(numbers, i, j):
    return sum(numbers) - (numbers[i] + numbers[j])

def get_closest_sum(target, numbers, length):
    closest_sum = float("inf")

    for i in range(length-1):
        for j in range(i+1, length):
            candidate = get_candidate(numbers, i, j)
            closest_sum = min(closest_sum, candidate)

    difference = abs(target - closest_sum)
    return difference


N, S = list(map(int, input().split()))
numbers = list(map(int, input().split()))

print(get_closest_sum(S, numbers, N))
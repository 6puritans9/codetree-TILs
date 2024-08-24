def is_possible(numbers, min_val, interval):
    available_indices = []
    for i, elem in enumerate(numbers):
        if elem >= min_val:
            available_indices.append(i)

    arr_size = len(available_indices)
    for i in range(1, arr_size):
        dist = available_indices[i] - available_indices[i - 1]
        if dist > interval:
            return False

    return True


n, k = map(int, input().split())
numbers = list(map(int, input().split()))

answer = 0
for num in range(1, n):
    if is_possible(numbers, num, k):
        answer = max(answer, num)

print(answer)
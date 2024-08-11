def get_max_sum(numbers, size, sub_size):
    max_sum = 0
    for i in range(size - sub_size + 1):
        max_sum = max(max_sum, sum(numbers[i:i+sub_size]))

    return max_sum


n, k = list(map(int, input().split()))
numbers = list(map(int, input().split()))

print(get_max_sum(numbers, n, k))
def in_range(x, n):
    return 0 <= x < n


def jump(numbers, n, idx, count):
    global min_count

    # if not in_range(idx, n) or max_jump_dist == 0:
    #     return

    if idx >= n - 1:
        min_count = min(min_count, count)
        return

    max_jump_dist = numbers[idx]

    for i in range(1, max_jump_dist + 1):
        jump(numbers, n, idx + i, count + 1)


if __name__ == "__main__":
    n = int(input())
    numbers = [int(num) for num in input().split()]
    min_count = float("inf")

    jump(numbers, n, 0, 0)
    print(min_count if min_count != float("inf") else -1)

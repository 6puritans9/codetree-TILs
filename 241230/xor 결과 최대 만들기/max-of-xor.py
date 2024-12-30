def backtrack(numbers, idx, subsets, cur_subset):
    global n, m

    if len(cur_subset) == m:
        subsets.append(cur_subset[:])
        return
    if idx >= n:
        return

    cur_subset.append(numbers[idx])
    backtrack(numbers, idx + 1, subsets, cur_subset)
    cur_subset.pop()

    backtrack(numbers, idx + 1, subsets, cur_subset)


def generate_subsets(numbers):
    global n, m

    subsets = []
    backtrack(numbers, 0, subsets, [])
    return subsets


def find_max_xor(numbers):
    subsets = generate_subsets(numbers)

    max_xor = 0
    for subset in subsets:
        cur_xor = 0

        for number in subset:
            cur_xor ^= number
        max_xor = max(max_xor, cur_xor)

    return max_xor


if __name__ == "__main__":
    n, m = tuple(map(int, input().split()))
    integers = list(map(int, input().split()))

    result = find_max_xor(integers)
    print(result)

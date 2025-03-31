def get_h_index(n: int, numbers: list[int]) -> int:
    max_number = max(numbers)
    arr = [0 for _ in range(max_number + 1)]

    for number in numbers:
        arr[number] += 1

    papers = 0
    for h_index in range(max_number, -1, -1):
        papers += arr[h_index]

        if papers >= h_index:
            return h_index

    return 0


def increase_l_elements(n, l, numbers, start, count):
    if count > l:
        return get_h_index(n, numbers)
    if start == n:
        return 0

    max_h = 0

    for i in range(start, n):
        numbers[i] += 1
        max_h = max(max_h, increase_l_elements(n, l, numbers, i + 1, count + 1))
        numbers[i] -= 1
    max_h = max(max_h, increase_l_elements(n, l, numbers, start + 1, count))

    return max_h


def find_max_h(n: int, l: int, numbers: list[int]) -> int:
    if not l:
        return get_h_index(n, numbers)

    return increase_l_elements(n, l, numbers, 0, 1)


if __name__ == "__main__":
    # Problem
    # For given N numbers,
    # add 1 to each L element
    # to maximize H.
    # This prolem asks h-index with a tweak,
    # which can easily be solved in counting sort in O(NK)

    # Constraints
    # 1 <= N <= 10^2
    # 0 <= L <= N
    # 0 <= element <= 10^2
    # Time 5000ms
    # Space 288 MiB

    # Approach
    # 1. I can get h-index for O(NK)
    #   which will increase to O(NK * nCl) == O(10^4 * 10^4) = 8/8 * 10^3ms
    # 2. This will occupy O(100) in space, which is easily managable

    # 3. Add 1 for L selected elements in nCl combination
    # 4. assign a counting sort array
    # 5. compare each result to find max_h
    # 6. return max_h

    n, l = map(int, input().split())
    numbers = [int(num) for num in input().split()]

    print(find_max_h(n, l, numbers))

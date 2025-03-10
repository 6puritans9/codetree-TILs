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


def compute_xor(num1, num2):
    result = 0
    bit_pos = 0

    while num1 > 0 or num2 > 0:
        bit1 = num1 & 1  # Extract the least significant bit of num1
        bit2 = num2 & 1  # Extract the least significant bit of num2

        xor_bit = bit1 ^ bit2  # XOR the bits
        result |= xor_bit << bit_pos  # Set the bit in the result

        num1 >>= 1  # Right shift num1 to process the next bit
        num2 >>= 1  # Right shift num2 to process the next bit
        bit_pos += 1  # Move to the next bit position

    return result


def find_max_xor(numbers):
    subsets = generate_subsets(numbers)

    max_xor = 0
    for subset in subsets:
        cur_xor = 0
        for number in subset:
            cur_xor = compute_xor(cur_xor, number)  # Manually compute XOR
        max_xor = max(max_xor, cur_xor)

    return max_xor


if __name__ == "__main__":
    n, m = tuple(map(int, input().split()))
    integers = list(map(int, input().split()))

    result = find_max_xor(integers)
    print(result)

def is_duplicate(sequence):
    length = len(sequence)
    for sub_len in range(1, length // 2 + 1):
        if sequence[-sub_len:] == sequence[-2 * sub_len:-sub_len]:
            return True
    return False


def backtrack(sequence, n):
    if len(sequence) == n:  # Base case: sequence is complete
        return True

    for num in [4, 5, 6]:  # Try each number in lexicographical order
        sequence.append(num)
        if not is_duplicate(sequence):  # Check if the sequence remains valid
            if backtrack(sequence, n):  # Recur to complete the sequence
                return True
        sequence.pop()  # Undo the choice if it leads to an invalid state

    return False  # No valid number could be appended


def get_sequence(n):
    sequence = []
    backtrack(sequence, n)
    return sequence


if __name__ == "__main__":
    n = int(input())
    sequence = get_sequence(n)
    print("".join(map(str, sequence)))
